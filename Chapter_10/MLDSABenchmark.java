/*
 * Example: ML-DSA levels comparison using Bouncy Castle 1.83
 *
 *
 * Author: Adapted by Miguel Vargas Martin from ChatGPT iterations
 * Last Modified: March 2026
 *
 * This example illustrates:
 *   1. Key generation
 *   2. Structure of the public key
 *   3. How the public seed (rho) is embedded
 */
 
package MLDSABenchmark;
import java.security.*;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

import org.bouncycastle.jcajce.spec.MLDSAParameterSpec;

//import org.bouncycastle.pqc.jcajce.spec.MLDSAParameterSpec;

public class MLDSABenchmark {

    private static final byte[] MESSAGE =
            "This is a document that will be signed using ML-DSA.".getBytes();

    public static void main(String[] args) throws Exception {

        Security.addProvider(new BouncyCastleProvider());

        testMLDSA("ML-DSA-44", MLDSAParameterSpec.ml_dsa_44);
        testMLDSA("ML-DSA-65", MLDSAParameterSpec.ml_dsa_65);
        testMLDSA("ML-DSA-87", MLDSAParameterSpec.ml_dsa_87);
    }

    private static void testMLDSA(String name, MLDSAParameterSpec spec) throws Exception {

        System.out.println("----- " + name + " -----");

        KeyPairGenerator kpg = KeyPairGenerator.getInstance("MLDSA", "BC");
        kpg.initialize(spec, new SecureRandom());
        
        int ITERATIONS = 10;

        for(int i=0;i<ITERATIONS;i++){
            kpg.generateKeyPair();
        }

        // Key generation
        long startKey = System.nanoTime();
        KeyPair kp = kpg.generateKeyPair();
        long endKey = System.nanoTime();
        long keyGenTime = (endKey - startKey) / 1_000_000;

        // Signing
        Signature signer = Signature.getInstance("MLDSA", "BC");
        signer.initSign(kp.getPrivate());

        long startSign = System.nanoTime();
        signer.update(MESSAGE);
        byte[] signature = signer.sign();
        long endSign = System.nanoTime();
        long signTime = (endSign - startSign) / 1_000_000;

        // Verification
        Signature verifier = Signature.getInstance("MLDSA", "BC");
        verifier.initVerify(kp.getPublic());

        long startVerify = System.nanoTime();
        verifier.update(MESSAGE);
        boolean valid = verifier.verify(signature);
        long endVerify = System.nanoTime();
        long verifyTime = (endVerify - startVerify) / 1_000_000;

        System.out.println("Public Key Generation Time: " + keyGenTime + " ms");
        System.out.println("Signing Time: " + signTime + " ms");
        System.out.println("Verification Time: " + verifyTime + " ms");
        System.out.println("Signature Size: " + signature.length + " bytes");
        System.out.println("Signature Valid: " + valid);
        System.out.println();
    }
}