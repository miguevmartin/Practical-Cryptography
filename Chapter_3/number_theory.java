/*
* TODO-based exploration of number theory with SymPy.
* Author: ChatGPT with small adaptations by Miguel Vargas Martin
* Last modified: January 2026
*
* Instructions:
* - Read each TODO carefully.
* - Before running a line, try to predict its output.
* - Uncomment lines only when instructed.
* - Answer the questions in the comments or in a separate worksheet.
*/

import java.math.BigInteger;
import java.util.*;

import org.apache.commons.math3.util.ArithmeticUtils;
import org.apache.commons.math3.primes.Primes;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

import java.security.Security;

public class NumberTheoryExploration {

    public static void main(String[] args) {

        Security.addProvider(new BouncyCastleProvider());

        // TODO 1: Basic integers

        int a = 3, b = 18, n = 25;

        // TODO 1.1: GCD
        System.out.println("gcd(a,b) = " + ArithmeticUtils.gcd(a, b));

        // TODO 1.2: LCM
        System.out.println("lcm(a,b) = " + ArithmeticUtils.lcm(a, b));

        // TODO 1.3: Divisors of n
        System.out.println("Divisors of n:");
        for (int d = 1; d <= n; d++) {
            if (n % d == 0) {
                System.out.print(d + " ");
            }
        }
        System.out.println();

        // TODO 1.4: Number of divisors
        int divisorCount = 0;
        for (int d = 1; d <= n; d++) {
            if (n % d == 0) divisorCount++;
        }
        System.out.println("Number of divisors of n = " + divisorCount);

        // TODO 1.5: Prime factorization
        System.out.println("Prime factorization of n:");
        factorize(n);

        // TODO 2: Primality
        System.out.println("Is n prime? " + Primes.isPrime(n));

        // TODO 3: Euler's Totient Function
        System.out.println("phi(a) = " + totient(a));
        System.out.println("phi(b) = " + totient(b));
        System.out.println("phi(n) = " + totient(n));

        // TODO 4: Chinese Remainder Theorem (CRT)
        BigInteger[] moduli = {
            BigInteger.valueOf(99),
            BigInteger.valueOf(97),
            BigInteger.valueOf(95)
        };

        BigInteger[] residues = {
            BigInteger.valueOf(49),
            BigInteger.valueOf(76),
            BigInteger.valueOf(65)
        };

        BigInteger crtSolution = chineseRemainder(residues, moduli);
        System.out.println("CRT solution x = " + crtSolution);

        // TODO 5: Miller–Rabin Primality Test
        BigInteger test = BigInteger.valueOf(1_373_651);
        System.out.println("Miller–Rabin result: " +
                test.isProbablePrime(10));

        // TODO 6: Primitive Roots (limited implementation)
        System.out.println("Primitive root modulo 25:");
        System.out.println(findPrimitiveRoot(25));

        // TODO 7: Discrete Logarithm (brute-force demo)
        System.out.println("Solving 7^x ≡ 15 (mod 41)");
        System.out.println("x = " + discreteLog(7, 15, 41));
    }

    // ------------------ Helpers ------------------
    static void factorize(int n) {
        int x = n;
        for (int p = 2; p * p <= x; p++) {
            while (x % p == 0) {
                System.out.print(p + " ");
                x /= p;
            }
        }
        if (x > 1) System.out.print(x);
        System.out.println();
    }

    static int totient(int n) {
        int result = n;
        for (int p = 2; p * p <= n; p++) {
            if (n % p == 0) {
                while (n % p == 0) n /= p;
                result -= result / p;
            }
        }
        if (n > 1) result -= result / n;
        return result;
    }

    static BigInteger chineseRemainder(BigInteger[] a, BigInteger[] m) {
        BigInteger M = BigInteger.ONE;
        for (BigInteger mi : m) M = M.multiply(mi);

        BigInteger result = BigInteger.ZERO;
        for (int i = 0; i < m.length; i++) {
            BigInteger Mi = M.divide(m[i]);
            BigInteger inv = Mi.modInverse(m[i]);
            result = result.add(a[i].multiply(Mi).multiply(inv));
        }
        return result.mod(M);
    }

    static int findPrimitiveRoot(int n) {
        if (totient(n) <= 2) return -1;
        int phi = totient(n);

        for (int g = 2; g < n; g++) {
            Set<Integer> seen = new HashSet<>();
            int x = 1;
            for (int i = 0; i < phi; i++) {
                x = (x * g) % n;
                seen.add(x);
            }
            if (seen.size() == phi) return g;
        }
        return -1;
    }

    static int discreteLog(int base, int target, int mod) {
        int value = 1;
        for (int x = 0; x < mod; x++) {
            if (value == target) return x;
            value = (value * base) % mod;
        }
        return -1;
    }
}
