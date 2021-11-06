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

    public static String encrypt(String message, SecretKeySpec key, IvParameterSpec iv) {
        String cipherText = null;
        try {
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            cipher.init(Cipher.ENCRYPT_MODE, key, iv);
            cipherText = Base64.getEncoder().encodeToString(cipher.doFinal(message.getBytes("UTF-8")));
        } catch (Exception e) {
            e.printStackTrace();
        }
        return cipherText;
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

    public static void main(String args[]) throws Exception {

        byte[] key = Base64.getUrlDecoder().decode("1e_zL72nMuNAomwDlWpH9Tc-a8QVwpilX7xe4V-TTkE=");
        byte[] fToken = Base64.getUrlDecoder().decode("gAAAAABhhI-hlpDqzwbgf93PYj1laIn8yJkYy2mMqoyVORRMHgU4VUcgJLHEoULHh_dx9oIq0xG_-SYvcM3U3w556fqx56ddIvGseHpYfw-vaznprtfKyVg=");

        byte[] cipherKeyBytes = Arrays.copyOfRange(key, 16, 32);
        byte[] signKeyBytes = Arrays.copyOfRange(key, 0, 16);
        SecretKeySpec signKey = new SecretKeySpec(signKeyBytes, "HmacSHA256");
        SecretKeySpec cipherKey = new SecretKeySpec(cipherKeyBytes, "AES");

        byte[] ivBytes = Arrays.copyOfRange(fToken, 9, 25);
        IvParameterSpec iv = new IvParameterSpec(ivBytes);

        byte[] cipherText = Arrays.copyOfRange(fToken, 25, fToken.length - 32);
        byte[] TokenHMAC = Arrays.copyOfRange(fToken, fToken.length - 32, fToken.length);
        byte[] HMACCalc = HMAC(Arrays.copyOfRange(fToken, 0, fToken.length - 32), signKey);

        System.out.print("token mac: ");
        System.out.println(Base64.getUrlEncoder().encodeToString(TokenHMAC));
        System.out.print("calc mac: ");
        System.out.println(Base64.getUrlEncoder().encodeToString(HMACCalc));

        if (Arrays.equals(TokenHMAC, HMACCalc)) {
            System.out.println("MACs match!");
        } else {
            System.out.println("MACs don't match!");
        }

        String finalMsg = decrypt(cipherText, cipherKey, iv);
        System.out.println(finalMsg);
    }
}