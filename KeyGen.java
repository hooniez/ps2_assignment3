import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.KeyGenerator;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

import java.security.Key;
import java.security.SecureRandom;



import java.util.Base64;



public class KeyGen {

    public static Byte[] HMAC(String message, Byte[] key) {
        final public String algo = "HmacSHA256";
        Mac mac = Mac.getInstance(algo);
        SecretKeySpec secretKeySpec = new SecretKeySpec(key, algo);
        return 
    }

    public static String encrypt(String message, Key key, IvParameterSpec iv) {
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

    public static String decrypt(String cipherText, Key key, IvParameterSpec iv) {
        String decryptedMsg = null;
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
        KeyGenerator keyGenerator = KeyGenerator.getInstance("AES");
        keyGenerator.init(128);
        SecretKey key = keyGenerator.generateKey();

        SecureRandom secRand = new SecureRandom();
        IvParameterSpec iv = new IvParameterSpec(secRand.generateSeed(16));

        System.out.println(Base64.getEncoder().encodeToString(key.getEncoded()));
        String cipherText = encrypt("hello world 1234", key, iv);
        System.out.println(cipherText);

        String finalMsg = decrypt(cipherText, key, iv);
        System.out.println(finalMsg);
    }
}