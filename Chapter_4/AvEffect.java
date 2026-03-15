/*
* Avalanche Effect Exploration using Triple DES (3DES)
* 
* This program illustrates how small changes in the key or plaintext
* may (or may not!) affect the ciphertext, depending on the cipher
* and mode of operation.
*
* Last modified: February 2026
* Author: ChatGPT with some modifications by Miguel Vargas Martin
*/

import org.bouncycastle.crypto.engines.DESedeEngine;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.crypto.BufferedBlockCipher;
import org.bouncycastle.crypto.modes.ECBBlockCipher;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

import java.security.Security;
import java.util.Arrays;

public class AvalancheEffect3DES {

    static {
        Security.addProvider(new BouncyCastleProvider());
    }

    /**
     * Compute the Hamming distance (bitwise) between two byte arrays.
     * Both arrays must have the same length.
     */
    public static int hamming(byte[] a, byte[] b) {
        if (a.length != b.length) {
            throw new IllegalArgumentException("Inputs must have equal length");
        }

        int distance = 0;
        for (int i = 0; i < a.length; i++) {
            distance += Integer.bitCount(a[i] ^ b[i]);
        }
        return distance;
    }

    /**
     * Encrypt a single block-aligned plaintext using 3DES in ECB mode.
     */
    public static byte[] encrypt(byte[] key, byte[] plaintext) throws Exception {
        BufferedBlockCipher cipher =
                new BufferedBlockCipher(new ECBBlockCipher(new DESedeEngine()));

        cipher.init(true, new KeyParameter(key));

        byte[] output = new byte[cipher.getOutputSize(plaintext.length)];
        int len = cipher.processBytes(plaintext, 0, plaintext.length, output, 0);
        cipher.doFinal(output, len);

        return output;
    }

    public static void main(String[] args) throws Exception {

        // Key setup
        byte[] k1 = "12345678".repeat(3).getBytes();
        byte[] k2 = "123456781234567812345679".getBytes();

        // Same plaintext, different (closely related) keys
        byte[] plaintext = "a secret message".getBytes();

        byte[] ct1 = encrypt(k1, plaintext);
        byte[] ct2 = encrypt(k2, plaintext);

        System.out.println(
            "Avalanche effect (same plaintext, different keys): "
            + hamming(ct1, ct2)
        );

        // Plaintext avalanche effect
        byte[] p1 = "a secret".getBytes();
        byte[] p2 = "a secreu".getBytes(); // differs by one bit

        byte[] ct3 = encrypt(k1, p1);
        byte[] ct4 = encrypt(k1, p2);

        System.out.println(
            "Avalanche effect (different plaintexts, same key): "
            + hamming(ct3, ct4)
        );

        // Sanity check for students
        System.out.println(
            "Hamming distance of plaintexts: "
            + hamming(p1, p2)
        );
    }
}
