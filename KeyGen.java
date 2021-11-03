import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

import java.security.Key;
import java.security.SecureRandom;
import java.security.MessageDigest;
import java.util.Arrays;

import java.util.Base64;



public class KeyGen {

    public static SecretKeySpec generateSecretKey(String myKey) {
        MessageDigest sha = null;
        byte[] key;
        SecretKeySpec secretKey = null;
        try {
            key = myKey.getBytes("UTF-8");
            sha = MessageDigest.getInstance("SHA-1");
            key = sha.digest(key);
            key = Arrays.copyOf(key, 16); 
            secretKey = new SecretKeySpec(key, "AES");
        } 
        catch (Exception e) {
            e.printStackTrace();
        }

        return secretKey;
    }

    public static String encrypt(String message, Key key, IvParameterSpec iv) {
        String cipherText = null;
        try {
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            cipher.init(Cipher.ENCRYPT_MODE, key);
            cipherText = Base64.getEncoder().encodeToString(cipher.doFinal(message.getBytes("UTF-8")));
        } catch (Exception e) {
            e.printStackTrace();
        }
        return cipherText;
    }

    public static String decrypt(String cipherText, Key key, IvParameterSpec iv) {
        String decryptedMsg = null;
        System.out.println(key);
        try {
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            cipher.init(Cipher.DECRYPT_MODE, key, iv);
            decryptedMsg = new String(cipher.doFinal(Base64.getDecoder().decode(cipherText)));
        } catch (Exception e) {
            e.printStackTrace();
        }

        return decryptedMsg;
    }

    public static void main(String args[]) throws Exception {
        String myKey = "thisismysecretkey";
        SecretKeySpec SecretKey = generateSecretKey(myKey);
        SecureRandom secRand = new SecureRandom();
        IvParameterSpec iv = new IvParameterSpec(secRand.generateSeed(16));

        System.out.println(SecretKey);
        String cipherText = encrypt("hello world 1234", SecretKey, iv);
        System.out.println(cipherText);

        String finalMsg = decrypt(cipherText, SecretKey, iv);
        System.out.println(finalMsg);
    }
}