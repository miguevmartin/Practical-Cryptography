/*
 * Exercise 10.8
 *
 * Compare the times obtained from Exercise 10.7 against
 * a 2048-bit RSA signature.
 *
 * Modified: March 2026
 * Author: ChatGPT and adapted by Miguel Vargas Martin
 *
 * This program benchmarks:
 * 1. ML-DSA-44
 * 2. ML-DSA-65
 * 3. ML-DSA-87
 * 4. RSA-2048 with RSA-PSS and SHA-256
 *
 * The same message is signed in all four cases.
 *
 * IMPORTANT:
 * - Times are implementation- and hardware-dependent.
 * - A short warm-up loop is used before timing so that
 *   JVM startup effects do not unfairly affect the first test.
 */

import java.security.*;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.jcajce.spec.MLDSAParameterSpec;
import java.security.spec.MGF1ParameterSpec;
import java.security.spec.PSSParameterSpec;

public class SignatureComparison {
    public static void main(String[] args) throws Exception {

        Security.addProvider(new BouncyCastleProvider());

        byte[] message =
            "This is a document that will be signed using ML-DSA and RSA."
            .getBytes();

        int ITERATIONS = 10;

        long startKey, endKey;
        long startSign, endSign;
        long startVerify, endVerify;

        long keyGenTime, signTime, verifyTime;

        KeyPairGenerator kpg;
        KeyPair kp;
        Signature signer;
        Signature verifier;
        byte[] signature;
        boolean valid;

        System.out.println("========================================");
        System.out.println("ML-DSA-44");
        System.out.println("========================================");

        kpg = KeyPairGenerator.getInstance("MLDSA", "BC");
        kpg.initialize(MLDSAParameterSpec.ml_dsa_44, new SecureRandom());

        for (int i = 0; i < ITERATIONS; i++) {
            kpg.generateKeyPair();
        }

        startKey = System.nanoTime();
        kp = kpg.generateKeyPair();
        endKey = System.nanoTime();
        keyGenTime = (endKey - startKey) / 1_000_000;

        signer = Signature.getInstance("MLDSA", "BC");
        signer.initSign(kp.getPrivate());
        startSign = System.nanoTime();
        signer.update(message);
        signature = signer.sign();
        endSign = System.nanoTime();
        signTime = (endSign - startSign) / 1_000_000;

        verifier = Signature.getInstance("MLDSA", "BC");
        verifier.initVerify(kp.getPublic());
        startVerify = System.nanoTime();
        verifier.update(message);
        valid = verifier.verify(signature);
        endVerify = System.nanoTime();
        verifyTime = (endVerify - startVerify) / 1_000_000;

        System.out.println("Public Key Generation Time: " + keyGenTime + " ms");
        System.out.println("Signing Time: " + signTime + " ms");
        System.out.println("Verification Time: " + verifyTime + " ms");
        System.out.println("Signature Size: " + signature.length + " bytes");
        System.out.println("Signature Valid: " + valid);
        System.out.println();

        System.out.println("========================================");
        System.out.println("ML-DSA-65");
        System.out.println("========================================");

        kpg = KeyPairGenerator.getInstance("MLDSA", "BC");
        kpg.initialize(MLDSAParameterSpec.ml_dsa_65, new SecureRandom());

        for (int i = 0; i < ITERATIONS; i++) {
            kpg.generateKeyPair();
        }

        startKey = System.nanoTime();
        kp = kpg.generateKeyPair();
        endKey = System.nanoTime();
        keyGenTime = (endKey - startKey) / 1_000_000;

        signer = Signature.getInstance("MLDSA", "BC");
        signer.initSign(kp.getPrivate());
        startSign = System.nanoTime();
        signer.update(message);
        signature = signer.sign();
        endSign = System.nanoTime();
        signTime = (endSign - startSign) / 1_000_000;

        verifier = Signature.getInstance("MLDSA", "BC");
        verifier.initVerify(kp.getPublic());
        startVerify = System.nanoTime();
        verifier.update(message);
        valid = verifier.verify(signature);
        endVerify = System.nanoTime();
        verifyTime = (endVerify - startVerify) / 1_000_000;

        System.out.println("Public Key Generation Time: " + keyGenTime + " ms");
        System.out.println("Signing Time: " + signTime + " ms");
        System.out.println("Verification Time: " + verifyTime + " ms");
        System.out.println("Signature Size: " + signature.length + " bytes");
        System.out.println("Signature Valid: " + valid);
        System.out.println();

        System.out.println("========================================");
        System.out.println("ML-DSA-87");
        System.out.println("========================================");

        kpg = KeyPairGenerator.getInstance("MLDSA", "BC");
        kpg.initialize(MLDSAParameterSpec.ml_dsa_87, new SecureRandom());

        for (int i = 0; i < ITERATIONS; i++) {
            kpg.generateKeyPair();
        }

        startKey = System.nanoTime();
        kp = kpg.generateKeyPair();
        endKey = System.nanoTime();
        keyGenTime = (endKey - startKey) / 1_000_000;

        signer = Signature.getInstance("MLDSA", "BC");
        signer.initSign(kp.getPrivate());
        startSign = System.nanoTime();
        signer.update(message);
        signature = signer.sign();
        endSign = System.nanoTime();
        signTime = (endSign - startSign) / 1_000_000;

        verifier = Signature.getInstance("MLDSA", "BC");
        verifier.initVerify(kp.getPublic());
        startVerify = System.nanoTime();
        verifier.update(message);
        valid = verifier.verify(signature);
        endVerify = System.nanoTime();
        verifyTime = (endVerify - startVerify) / 1_000_000;

        System.out.println("Public Key Generation Time: " + keyGenTime + " ms");
        System.out.println("Signing Time: " + signTime + " ms");
        System.out.println("Verification Time: " + verifyTime + " ms");
        System.out.println("Signature Size: " + signature.length + " bytes");
        System.out.println("Signature Valid: " + valid);
        System.out.println();

        System.out.println("========================================");
        System.out.println("RSA-2048");
        System.out.println("========================================");

        kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(2048, new SecureRandom());

        for (int i = 0; i < ITERATIONS; i++) {
            kpg.generateKeyPair();
        }

        startKey = System.nanoTime();
        kp = kpg.generateKeyPair();
        endKey = System.nanoTime();
        keyGenTime = (endKey - startKey) / 1_000_000;

        PSSParameterSpec pssSpec = new PSSParameterSpec(
            "SHA-256",
            "MGF1",
            MGF1ParameterSpec.SHA256,
            32,
            1
        );

        signer = Signature.getInstance("RSASSA-PSS");
        signer.setParameter(pssSpec);
        signer.initSign(kp.getPrivate());
        startSign = System.nanoTime();
        signer.update(message);
        signature = signer.sign();
        endSign = System.nanoTime();
        signTime = (endSign - startSign) / 1_000_000;

        verifier = Signature.getInstance("RSASSA-PSS");
        verifier.setParameter(pssSpec);
        verifier.initVerify(kp.getPublic());
        startVerify = System.nanoTime();
        verifier.update(message);
        valid = verifier.verify(signature);
        endVerify = System.nanoTime();
        verifyTime = (endVerify - startVerify) / 1_000_000;

        System.out.println("Public Key Generation Time: " + keyGenTime + " ms");
        System.out.println("Signing Time: " + signTime + " ms");
        System.out.println("Verification Time: " + verifyTime + " ms");
        System.out.println("Signature Size: " + signature.length + " bytes");
        System.out.println("Signature Valid: " + valid);
        System.out.println();
    }
}