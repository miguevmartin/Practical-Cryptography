/*
 * Example: ML-KEM-768 (formerly Kyber-768) using Bouncy Castle 1.83
 *
 * IMPORTANT:
 * Starting with Bouncy Castle 1.83, the original "Kyber" classes
 * were replaced with ML-KEM classes to match the finalized NIST
 * FIPS 203 standard.
 *
 * ML-KEM-768 ≡ Kyber-768 (k = 3).
 *
 * Author: Adapted by Miguel Vargas Martin from ChatGPT iterations
 * Last Modified: February 2026
 *
 * This example illustrates:
 *   1. Key generation
 *   2. Structure of the public key
 *   3. How the public seed (rho) is embedded
 */

import org.bouncycastle.pqc.crypto.mlkem.*;
import org.bouncycastle.crypto.AsymmetricCipherKeyPair;
import org.bouncycastle.util.encoders.Hex;
import java.security.SecureRandom;

public class KyberMatrix {

    public static void main(String[] args) {
        /*
         * 1. Select Parameter Set
         *
         * ML-KEM defines three security levels:
         *   ml_kem_512   (k = 2)
         *   ml_kem_768   (k = 3)  ← recommended / balanced
         *   ml_kem_1024  (k = 4)
         *
         * For ML-KEM-768:
         *   - k = 3
         *   - Matrix A is 3 × 3
         *   - Each element is a polynomial of degree 255
         *   - Arithmetic is over Z_q[x]/(x^256 + 1)
         */
        MLKEMParameters params = MLKEMParameters.ml_kem_768;

        /*
         * 2. Key Generation
         *
         * Internally, the algorithm:
         *   - Generates 32 random bytes (seed d)
         *   - Expands d into:
         *         rho   → public matrix seed
         *         sigma → noise seed
         *   - Uses rho to deterministically generate matrix A
         *   - Samples secret vector s and noise vector e
         *   - Computes:
         *         t = A·s + e
         * The public key is:
         *         (t, rho)
         * The private key contains:
         *         s and additional values for decapsulation
         */
        MLKEMKeyPairGenerator keyGen = new MLKEMKeyPairGenerator();
        keyGen.init(new MLKEMKeyGenerationParameters(
                new SecureRandom(), params));
        AsymmetricCipherKeyPair keyPair = keyGen.generateKeyPair();
        MLKEMPublicKeyParameters pubKey =
                (MLKEMPublicKeyParameters) keyPair.getPublic();
        MLKEMPrivateKeyParameters privKey =
                (MLKEMPrivateKeyParameters) keyPair.getPrivate();
        System.out.println("=== ML-KEM-768 Key Generation ===");

        /*
         * 3. Encoded Public Key Structure
         *
         * Bouncy Castle does NOT expose:
         *   - Matrix A
         *   - Vector t
         *   - Seed rho
         * Instead, it exposes a standardized byte encoding.
         * For ML-KEM-768, the public key encoding is:
         *     publicKey = t || rho
         * where:
         *     t   = compressed polynomial vector
         *     rho = 32-byte matrix seed
         */
        byte[] encodedPub = pubKey.getEncoded();
        System.out.println("Public key length: "
                + encodedPub.length + " bytes");

        /*
         * 4. Extracting the Matrix Seed (rho)
         *
         * In ML-KEM-768:
         *     rho is always the last 32 bytes
         *
         * rho is the seed that deterministically expands
         * (via SHAKE-128) into the full matrix A.
         *
         * Matrix A itself is never stored — it is generated
         * on-the-fly during encapsulation.
         */
        byte[] rho = new byte[32];
        System.arraycopy(
                encodedPub,
                encodedPub.length - 32,
                rho,
                0,
                32
        );

        System.out.println("Matrix seed (rho): "
                + Hex.toHexString(rho));

        /*
         * 5. Private Key
         *
         * The private key encoding contains:
         *   - Secret vector s
         *   - Hash of the public key
         *   - Randomness for CCA security
         * All internal lattice values remain hidden,
         * enforcing safe usage through encapsulation/decapsulation.
         */
        byte[] encodedPriv = privKey.getEncoded();
        System.out.println("Private key length: "
                + encodedPriv.length + " bytes");

        /*
         * Conceptual Summary
         *
         * ML-KEM does NOT store matrix A explicitly.
         * Instead:
         *   A = Expand(rho)
         * This design:
         *   ✓ reduces public key size
         *   ✓ ensures deterministic reconstruction
         *   ✓ simplifies interoperability
         *   ✓ avoids accidental misuse
         *
         * Bouncy Castle intentionally hides internal
         * polynomials to prevent cryptographic misuse.
         */
    }
}
