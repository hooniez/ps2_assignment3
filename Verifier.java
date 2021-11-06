package net.zhuoweizhang.raspberryjuice;

import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

import java.util.Arrays;
import java.util.Base64;


public class Verifier {
    

    private static byte[] HMAC(byte[] message, SecretKeySpec key) {
        final String algo = "HmacSHA256";
        byte[] macBytes = null;
        try {
            Mac mac = Mac.getInstance(algo);
            mac.init(key);
            macBytes = mac.doFinal(message);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return macBytes;
    }

    private static String decrypt(byte[] cipherText, SecretKeySpec key, IvParameterSpec iv) {
        String decryptedMsg = null;
        try {
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            cipher.init(Cipher.DECRYPT_MODE, key, iv);
            decryptedMsg = new String(cipher.doFinal(cipherText));
        } catch (Exception e) {
            e.printStackTrace();
        }

        return decryptedMsg;
    }



    public static String messageHandler(byte[] sharedKey, byte[] token) {
        String finalMsg = null;
        byte[] cipherKeyBytes = Arrays.copyOfRange(sharedKey, 16, 32);
        byte[] signKeyBytes = Arrays.copyOfRange(sharedKey, 0, 16);
        SecretKeySpec signKey = new SecretKeySpec(signKeyBytes, "HmacSHA256");
        SecretKeySpec cipherKey = new SecretKeySpec(cipherKeyBytes, "AES");

        byte[] ivBytes = Arrays.copyOfRange(token, 9, 25);
        IvParameterSpec iv = new IvParameterSpec(ivBytes);

        byte[] cipherText = Arrays.copyOfRange(token, 25, token.length - 32);
        byte[] TokenHMAC = Arrays.copyOfRange(token, token.length - 32, token.length);
        byte[] HMACCalc = HMAC(Arrays.copyOfRange(token, 0, token.length - 32), signKey);

        if (!Arrays.equals(TokenHMAC, HMACCalc)) {
            System.out.println("message cannot be verified");
        } else {
            finalMsg = decrypt(cipherText, cipherKey, iv);
        }
        return finalMsg;
    }
}