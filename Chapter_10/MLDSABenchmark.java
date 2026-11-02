/*
 * Example: ML-DSA levels comparison using Bouncy Castle 1.83
 *
 *
 * Author: Adapted by Miguel Vargas Martin from ChatGPT iterations
 * Last Modified: November 2026
 *
 * This example compares, for ML-DSA-44, ML-DSA-65 and ML-DSA-87:
 *   1. Key generation time
 *   2. Signing and verification time
 *   3. Signature size
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
        double keyGenTime = (endKey - startKey) / 1e6;

        // Signing
        Signature signer = Signature.getInstance("MLDSA", "BC");
        signer.initSign(kp.getPrivate());

        long startSign = System.nanoTime();
        signer.update(MESSAGE);
        byte[] signature = signer.sign();
        long endSign = System.nanoTime();
        double signTime = (endSign - startSign) / 1e6;

        // Verification
        Signature verifier = Signature.getInstance("MLDSA", "BC");
        verifier.initVerify(kp.getPublic());

        long startVerify = System.nanoTime();
        verifier.update(MESSAGE);
        boolean valid = verifier.verify(signature);
        long endVerify = System.nanoTime();
        double verifyTime = (endVerify - startVerify) / 1e6;

        System.out.println("Public Key Generation Time: " + keyGenTime + " ms");
        System.out.println("Signing Time: " + signTime + " ms");
        System.out.println("Verification Time: " + verifyTime + " ms");
        System.out.println("Signature Size: " + signature.length + " bytes");
        System.out.println("Signature Valid: " + valid);
        System.out.println();
    }
}