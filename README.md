# Practical Cryptography: From Classical Ciphers to Post-Quantum Standards
### Code Repository

© 2026 Miguel Vargas Martin

This repository contains the **Python and Java source code** accompanying the book:

**Practical Cryptography: From Classical Ciphers to Post-Quantum Standards**  
by **Miguel Vargas Martin**

The programs included here correspond to examples, demonstrations, and exercises presented throughout the book.

---

## Purpose of This Repository
The code is intended to support **learning and experimentation in applied cryptography**. It provides practical implementations of cryptographic concepts discussed in the text, including:

- Classical cryptography examples
- Symmetric encryption (AES and modes of operation)
- Hash functions and message authentication
- RSA encryption and digital signatures
- Number-theoretic algorithms used in cryptography
- Post-quantum cryptography (ML-KEM / Kyber and ML-DSA / Dilithium)

The goal of these examples is to help readers understand **how cryptographic algorithms work in practice**.

---

## Educational Use
The code in this repository is provided **for educational and non-commercial purposes**. It may be freely used for:

- personal learning
- university courses
- classroom demonstrations
- academic experimentation

Users are welcome to modify and adapt the programs for **teaching and research purposes**, provided appropriate credit is given.

---

## Important Security Notice
These programs are designed primarily for **instructional clarity**, not for production deployment.

Some examples intentionally demonstrate:

- insecure constructions
- deprecated algorithms
- simplified implementations

These cases are included to illustrate **important cryptographic pitfalls**.

**This code should not be used directly in production systems.**

---

## Environment
The examples were tested using:

### Python
- Python 3.11
- `cryptography` library

### Java
- Java 21 LTS
- Bouncy Castle cryptography provider

The code should work with most modern versions of these environments.

---

## Repository Structure
The code is organized by chapters corresponding to the book:

Contents
Part I Hidden in Plain Sight
1 Symbolic Geometric Ciphers
1.1 The Radar Cipher
1.2 Pigpen-ish Cipher (or an undisclosed cipher)
2 Steganography
2.1 Text Within Text
2.2 Text or Images in LSBs
2.3 Network Steganography
Part II Pre-Quantum Cryptography
3 Number Theory
3.1 Integers
3.2 Modular Arithmetic
3.3 Primes and Greatest Common Divisors
3.4 Greatest Common Divisors and Least Common Multiples
3.5 Multiplicative Inverse
3.6 Pre-Quantum One-Way Trapdoor Functions
3.6.1 Prime Factorization
3.6.2 Discrete Logarithms
3.7 Putting It All Together using SymPy
4 Symmetric Key Cryptography
4.1 Avalanche Effect
4.2 Advanced Encryption Standard
4.3 Key Wrapping
5 Digest Functions
5.1 Hash Functions
5.2 SHA-3 Hash and Extendable-Output Functions
5.3 Message Authentication Codes
6 Stream Ciphers and Random Numbers
6.1 Random Enough
6.2 Speed of Cryptographically Secure Generators
7 Public-Key Cryptography
7.1 RSA for Encryption
7.2 RSA for Digital Signatures
Part III Post-Quantum Cryptography
8 More Number Theory
8.1 Basic Number Theory for PQC
8.2 PQC One-Way Trapdoor Functions
9 ML-KEM Encapsulation
9.1 Encapsulation
9.2 Decapsulation
9.3 Key Generation
9.3.1 Seed generation and vector of polynomials A
9.3.2 Small vectors of polynomials s and e
9.3.3 Public key
9.4 ML-KEM Security Levels
10 ML-DSA Signature Standard
10.1 More Notation
10.2 ML-DSA Decomposition Algorithms
10.3 Signature Generation
10.3.1 Commitment generation
10.3.2 Challenge Derivation
10.3.3 Potential signature calculation
10.3.4 Rejection sampling
10.4 Signature Verification
10.4.1 Initial validation and derivations
10.4.2 Challenge derivation
10.4.3 Verification
10.5 Key Generation
10.5.1 Sampling seeds
10.5.2 Expanding the public matrix A
10.5.3 Generating the secret vectors (s1, s2)
10.5.4 Computing the public vector t
10.5.5 Compressing the public key t
10.6 One More One-Way Trapdoor Function: I-MSIS
10.7 ML-DSA Security Levels
Part IV Requiem
11 Beyond

Each directory contains the programs referenced in the corresponding chapter of the book.

---

## Contributing
Corrections, improvements, and bug reports are welcome.

If you discover an issue with the code, please open an issue or submit a pull request.

---

## License
This code is released under the **Creative Commons Attribution–NonCommercial 4.0 International License (CC BY-NC 4.0)**.

See the LICENSE file for details.
