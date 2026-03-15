/**
 * Demonstration of SHAKE128 using Bouncy Castle.
 *
 * SHAKE128 is an Extendable Output Function (XOF) defined in FIPS 202.
 * Unlike SHA-256 or SHA-3-256, SHAKE allows arbitrary-length output.
 *
 * Internally, SHAKE is based on the Keccak sponge construction.
 * 
 * Author: ChatGPT, modified by Miguel Vargas Martin
 *
 * Last modified: February 2026
 */

import org.bouncycastle.crypto.digests.SHAKEDigest;
import org.bouncycastle.util.encoders.Hex;

public class SHAKE128 {

    public static void main(String[] args) {

        // Input message to be hashed
        String input = "example data";

        // Convert the input string to bytes (UTF-8 encoding is recommended explicitly)
        byte[] inputBytes = input.getBytes();

 
        // 1. Initialize SHAKE128
         // The parameter (128) indicates 128-bit security strength.
        // This does NOT mean the output is 128 bits long.
        // Output length is chosen during the squeezing phase.
        SHAKEDigest digest = new SHAKEDigest(128);

         // 2. Absorb phase (update the sponge with input data)
         // The update() method feeds data into the sponge construction.
        // Parameters:
        //   - input array
        //   - offset (start position)
        //   - length (number of bytes to read)
        digest.update(inputBytes, 0, inputBytes.length);

         // 3. Squeeze phase (extract output bytes)
         // SHAKE is an XOF: we can request as many output bytes as needed.
        // Here, we request 64 bytes (512 bits).
        byte[] output = new byte[64];

        // doOutput() extracts bytes from the sponge.
        // If more bytes are requested later, squeezing continues.
        digest.doOutput(output, 0, output.length);

        // Convert the output to hexadecimal for readable display
        System.out.println("SHAKE128 Output (64 bytes): " + Hex.toHexString(output));
    }
}

