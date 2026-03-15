/*
 * Modified: February 2026
 * 
 * Author: Adapted by Miguel Vargas Martin from ChatGPT iterations
 * 
 * Kyber (ML-KEM) Benchmark Example
 *
 * This program measures:
 *   1. Key pair generation time
 *   2. Encapsulation time (key wrapping)
 *   3. Decapsulation time (key unwrapping)
 *
 * IMPORTANT:
 * Kyber is a Key Encapsulation Mechanism (KEM), not a traditional
 * public-key encryption scheme. Therefore, in Bouncy Castle it
 * only supports WRAP_MODE and UNWRAP_MODE.
 *
 * The program performs multiple iterations and reports
 * average execution times in milliseconds.
 */

import java.security.*;
import javax.crypto.*;

import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.pqc.jcajce.provider.BouncyCastlePQCProvider;
import org.bouncycastle.pqc.jcajce.spec.KyberParameterSpec;

public class Kyber {

    // Number of benchmark repetitions
    // Increase this for more stable timing results
    private static final int ITERATIONS = 100;

    public static void main(String[] args) throws Exception {
        /*
         * 1. Register Security Providers
         * BouncyCastleProvider  -> classical crypto algorithms
         * BouncyCastlePQCProvider -> post-quantum algorithms (Kyber, Dilithium, etc.)
         *
         * "BCPQC" is the provider name used later when requesting instances.
         */
        Security.addProvider(new BouncyCastleProvider());
        Security.addProvider(new BouncyCastlePQCProvider());

        // Accumulators for total execution time (in nanoseconds)
        long totalKeyGen = 0;
        long totalEncap = 0;
        long totalDecap = 0;

        /*
         * Main benchmark loop.
         * Each iteration performs a complete KEM cycle:
         *   - Generate Kyber keypair
         *   - Encapsulate (wrap a symmetric key)
         *   - Decapsulate (unwrap it)
         */
        for (int i = 0; i < ITERATIONS; i++) {
            // 2. Key Pair Generation
            /*
             * KyberParameterSpec.kyber768 selects the security level.
             * Available parameter sets:
             *   kyber512  -> NIST Level 1
             *   kyber768  -> NIST Level 3
             *   kyber1024 -> NIST Level 5
             * kyber768 is a good balanced choice for benchmarking.
             */
            long startKeyGen = System.nanoTime();

            KeyPairGenerator kpg =
                    KeyPairGenerator.getInstance("Kyber", "BCPQC");

            kpg.initialize(KyberParameterSpec.kyber768, new SecureRandom());

            KeyPair kp = kpg.generateKeyPair();

            long endKeyGen = System.nanoTime();
            totalKeyGen += (endKeyGen - startKeyGen);

            // 3. Encapsulation (WRAP_MODE)
            /*
             * Kyber encapsulates a randomly generated shared secret.
             * In JCA abstraction, this is modeled as wrapping a symmetric key.
             *
             * We generate a 256-bit AES key to simulate hybrid encryption.
             */
            KeyGenerator aesGen = KeyGenerator.getInstance("AES");
            aesGen.init(256);
            SecretKey secretKey = aesGen.generateKey();

            Cipher wrapCipher =
                    Cipher.getInstance("Kyber", "BCPQC");
            long startEncap = System.nanoTime();

            /*
             * WRAP_MODE triggers Kyber encapsulation.
             * Internally:
             *   - A shared secret is derived
             *   - A ciphertext (encapsulation) is produced
             */
            wrapCipher.init(Cipher.WRAP_MODE, kp.getPublic());

            byte[] wrappedKey = wrapCipher.wrap(secretKey);

            long endEncap = System.nanoTime();
            totalEncap += (endEncap - startEncap);

            // 4. Decapsulation (UNWRAP_MODE)
            /*
             * UNWRAP_MODE triggers Kyber decapsulation.
             * The private key reconstructs the shared secret
             * from the encapsulated ciphertext.
             */
            Cipher unwrapCipher =
                    Cipher.getInstance("Kyber", "BCPQC");
            long startDecap = System.nanoTime();
            unwrapCipher.init(Cipher.UNWRAP_MODE, kp.getPrivate());
            Key unwrappedKey =
                    unwrapCipher.unwrap(wrappedKey,
                                        "AES",
                                        Cipher.SECRET_KEY);
            long endDecap = System.nanoTime();
            totalDecap += (endDecap - startDecap);

            // 5. Correctness Verification
            /*
             * Ensure that encapsulation/decapsulation
             * correctly reconstructed the symmetric key.
             */
            if (!java.util.Arrays.equals(
                    secretKey.getEncoded(),
                    unwrappedKey.getEncoded())) {
                throw new RuntimeException("Decapsulation failed!");
            }
        }

        // 6. Print Average Timing Results
        System.out.println("Iterations: " + ITERATIONS);
        System.out.printf("Average Key Generation Time: %.3f ms%n",
                totalKeyGen / 1e6 / ITERATIONS);
        System.out.printf("Average Encapsulation Time: %.3f ms%n",
                totalEncap / 1e6 / ITERATIONS);
        System.out.printf("Average Decapsulation Time: %.3f ms%n",
                totalDecap / 1e6 / ITERATIONS);
    }
}
