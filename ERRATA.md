# Practical Cryptography – Errata

This list corrects the original release of *Practical Cryptography: From Classical Ciphers to Post-Quantum Standards* (March 2026). All corrections are already in the current version of the book. Page numbers refer to the original release.

The complete, corrected source code is in this repository.

Corrections are grouped as [technical corrections](#technical-corrections) (statements, formulas or data that were wrong), [corrections to program listings](#corrections-to-program-listings), and [minor typographical corrections](#minor-typographical-corrections). A final section lists [other changes](#other-changes-in-the-current-version) in the current version that are not errors.

Last updated: November 4, 2026

## Technical corrections

These 40 corrections fix statements, formulas, data or references that were wrong in the original release.

| Page | Where | Original | Correction |
| --- | --- | --- | --- |
| xvii | List of Acronyms, LSB | Less significant bit | Least Significant Bit |
| xviii | List of Acronyms, OFB | Open Feedback Mode | Output Feedback Mode |
| 3 | Exercise 1.1, ciphertext | )135 (315) (180) 45) (225) (225 (270) )180 (225 225( 270) 45) )270 225) )45 | )135 (315) (180) 45) (225) 225) (270) )180 225) )225 (270) 45) )270 225) )45 |
| 11 | §2.3, item 4 | The sources categorize this method as a form of steganography (“covered writing”) rather than mere encryption. | Delete this sentence. |
| 17 | Proof of Theorem 3.4 | a ≡ b mod m) | a ≡ b (mod m) |
| 17 | Proof of Theorem 3.5, last line | a + c = b + d (mod m) | a + c ≡ b + d (mod m) |
| 17 | Theorem 3.6 | Let a, b, and n be integers | Let a, b, and n > 0 be integers |
| 17 | Negation of a universal quantifier | (“The are some”) | (“There are some”) |
| 18 | Proof of Theorem 3.7 | there’s an integer k (k < n) | there’s an integer k (1 < k < m) |
| 18 | Proof of Theorem 3.9 | satisfies p_x ≥ √n … p_i p_j ≥ √n √n = n | satisfies p_x > √n … p_i p_j > √n √n = n |
| 23 | §3.7, introduction | such as the Chinese Remainder Theorem or discrete logarithms. | such as the Chinese Remainder Theorem. (Discrete logarithms are covered in §3.6.2.) |
| 29 | §4.1 | an avalanche effect close to 50% after each round, including the final one. | an avalanche effect close to 50% after enough rounds, and at the output. |
| 29 | §4.1, plaintexts that differ by one bit | b"a secret" and b"a secres" | b"a secret" and b"a secreu" (t and s differ in three bits; t and u in one) |
| 38 | Exercise 4.2 | iv = ctr = '0123456789abcdef' | iv = ctr = b'0123456789abcdef' (a bytes value). Add to the solution: since the messages are 128 bits long and no padding is used, assume a one-block encryption. |
| 39 | Exercise 4.4 | P1 contains the phrase “Sovereign Artic” | P1 starts with the phrase “Sovereign Artic” [sic]. Add: Assume P1 and P2 are each 16 bytes long. |
| 40 | Exercise 4.6, solution | man-in-the-middle | meet-in-the-middle |
| 53 | §5.2, SHAKE-128 | the strength does not increase (or decrease) with the output length. | Requesting more output never raises the strength above 128 bits, but requesting too little lowers it: for a d-bit output, FIPS 202 gives collision resistance of min(d/2, 128) bits and preimage resistance of min(d, 128) bits. A 256-bit output is needed for the full 128-bit collision resistance. |
| 56 | Exercise 5.9 | the (now insecure) Digital Signature Algorithm | the (now withdrawn) Digital Signature Algorithm (withdrawn in FIPS 186-5) |
| 61 | Chapter 6 epigraph | “The punishment of every disordered mind is its own disorder.” | “For it is even as Thou hast appointed, that every inordinate affection should bring its own punishment.” (St. Augustine, *Confessions*; the original line was a paraphrase.) |
| 80 | Exercise 7.4, Signature 2 | first line ends with a stray “—” | Delete the “—”; the signature is unchanged otherwise. |
| 83 | Chapter 8, introduction | (cf. sections 3.13 and 3.14) | (cf. Section 3.6) |
| 83 | Chapter 8, introduction | approximately 200 logical qubits (thousands of physical qubits make one logical qubit) | approximately 200 logical qubits (each encoded across many physical qubits: 288 for every 12 logical ones in IBM’s “gross” code) |
| 84 | Definition 8.1 | these polynomials are reduced modulus an irreducible polynomial xⁿ + 1 | xⁿ + 1 is irreducible over the integers when n is a power of 2, but not over ℤ_q for the moduli of the standards. R_q = ℤ_q[x]/⟨xⁿ + 1⟩ is a commutative ring, not a field (see Remark 8.1 in the current version). |
| 86 | Definition 8.6 | Decision-Module Learning With Errors (MLWE) | Decision-Module Learning With Errors (D-MLWE) |
| 88 | Chapter 9, CBD formula | c = Σ aᵢ − s Σ bᵢ | c = Σ aᵢ − Σ bᵢ |
| 90 | §9.1, decompression rule | ⌈q/2⌉, and mᵢ = ⌈q/2⌉ when mᵢ = 1 | ⌈q/2⌋ (round to nearest), and Decompress_q(mᵢ, 1) = ⌈q/2⌋ = 1665 when mᵢ = 1 |
| 91 | §9.3.1 | SHA3-512 (cf. Exercise ??) | SHA3-512 (cf. Exercise 5.7) |
| 91 | §9.3.1 | A ∈ R_q^(k×ℓ) | A ∈ R_q^(k×k) |
| 91–92 | §9.3.1, ExpandA | bit shifts on the first two bytes (16 bits) of SHAKE-128(ρ ∥ i ∥ j), masked to 12 bits; retry with the next two bytes | ExpandA reads the output stream of SHAKE-128(ρ ∥ j ∥ i) three bytes at a time and splits them into two 12-bit values; each value ≥ q is rejected, until all 256 coefficients are accepted. |
| 92 | §9.3.2 | the error vector e ∈ S_η₂^k | the error vector e ∈ S_η₁^k (FIPS 203 samples both s and e with η₁ in key generation) |
| 105–107 | Exercises 10.5 and 10.6 | Toy parameters q = 23, γ₂ = (q − 1)/2 = 11, α = 22. With α = q − 1 there is only one high-bit window, so the exercises cannot show hints, and the solutions are incorrect. | Use q = 41, γ₂ = (q − 1)/8 = 5, α = 10 (m = 4 windows), w = [[3, 14, 24, 38], [9, 21, 33, 5]] and a shift of +2. Then h = [[0, 1, 1, 0], [0, 0, 0, 1]], w′ = [[5, 16, 26, 40], [11, 23, 35, 7]], and UseHint recovers w₁ = [[0, 1, 2, 0], [1, 2, 3, 0]]. See the current version for the full text. |
| 107, 112 | Tables 10.1 and 10.2 | Table 10.1 lists only ML-DSA-87; Table 10.2 gives ML-DSA-44 as AES-128 equivalent | One table now lists all three parameter sets. ML-DSA-44 is NIST category 2: at least AES-128, between AES-128 and AES-192. |
| 108 | §10.3.1 | y is generated by an expansion function that uses K | y is generated by expanding, with SHAKE-256, a seed derived from K, the message digest μ and 32 fresh random bytes |
| 108 | §10.3.2 | a 256-bit seed c̃ = SHAKE-256(μ ∥ w₁, 32) | c̃ is λ/4 bytes long: 32, 48 and 64 bytes for ML-DSA-44, ML-DSA-65 and ML-DSA-87 (c̃ = SHAKE-256(μ ∥ w₁, 64) for ML-DSA-87) |
| 109, 111 | §10.4.1 and §10.5.4 | tr = SHAKE-256(pk, 32) | tr = SHAKE-256(pk, 64) |
| 109 | §10.4.2 | Bob derives the commitment c … Then he computes the challenge w₁ | Bob derives the challenge c … Then he recovers the high bits of the commitment, w₁ |
| 111 | §10.5.5 | compute the challenge w … an approximate value to w = Az − ct as w′ ≈ Az − c(t₁·2^d) | recover the high bits w₁ of the commitment … an approximate value of Az − ct as w′ = Az − c(t₁·2^d); w′ differs from Az − ct by c·t₀, the contribution of the missing low bits t₀ |
| 111 | §10.6, Definitions 10.1 and 10.2 | bounded by a small threshold B < q | bounded by a small threshold B ≪ q |
| 112 | §10.6 | Therefore Az − ct = 2γ₂ + w₁ + w₀ | Therefore Az − ct = 2γ₂w₁ + w₀ |
| 112 | Exercise 10.7, solution | Listing 9.3 offers a solution. Note the use of a loop of signature generations | Listing 10.5 offers a solution. Note the loop of key generations at the beginning, a warm-up |

## Corrections to program listings

Five listings in Chapter 10 had errors; the corrected files are in the [Chapter_10](Chapter_10) folder.

| Page | Listing | Problem | Correction |
| --- | --- | --- | --- |
| 100 | Listing 10.1 (Power2Round, scalars) | example = random.randint(0, q) can return q, which is outside [0, q − 1], because Python’s randint includes its upper bound. | Use random.randint(0, q - 1), and reduce the input first with r = r % q. |
| 102–103 | Listing 10.3 (Power2Round, vectors) | The function uses two_d and half_two_d, which are defined only as global variables later in the program. | Define two_d = 1 << d and half_two_d = 1 << (d - 1) inside the function. |
| 105 | Listing 10.4 (Decompose) | The overflow check is_handled = np.any((v1 == 0) & (v0 == -1)) does not detect the wrap-around case, and the toy values used q = 23. | is_handled = np.any((v1 == 0) & (vector_r % q > q - 1 - alpha // 2)), with the toy parameters q = 41, γ₂ = (q − 1)/8 and the vector of Exercise 10.5. |
| 112–115 | Listing 10.5 (ML-DSA benchmark) | Times are computed as long values divided by 1_000_000, an integer division, so sub-millisecond operations print 0 ms. The header comment described a different program (the structure of the public key). | Declare the times as double and divide by 1e6. The header now lists what the program compares: key generation time, signing and verification time, and signature size. |
| 115–119 | Listing 10.6 (ML-DSA vs RSA-2048) | Same integer division of times by 1_000_000. | Declare the times as double and divide by 1e6. |

## Minor typographical corrections

These typos do not change the meaning.

| Page | Where | Original | Correction |
| --- | --- | --- | --- |
| 5 | Exercise 1.1, solution | Data Encryption standard | Data Encryption Standard |
| 10 | Figure 2.1 caption | to establishing a steganographic channel | to establish a steganographic channel |
| 16 | §3.2 | ramainder | remainder |
| 19 | Footnote on Fermat | Keith Delvin’s | Keith Devlin’s |
| 38 | Exercise 4.2, solution | hamming distance | Hamming distance |
| 83 | Chapter 8, footnote 1 | Peter Shore | Peter Shor |
| 83 | Chapter 8, footnote 2 | visit NIST’ | visit NIST’s |
| 85 | Listing 8.1 caption | Symmetric module. | Symmetric modulo. |
| 85 | §8.1 | infinite norm | infinity norm |
| 90 | §9.2 | “bleed’ | “bleed” |
| 100 | §10.2 | Power2Run | Power2Round |
| 111 | §10.6, first sentence | ML-WE | MLWE |

## Other changes in the current version

The current version also adds explanations and material that were not errors in the original release:

- **Chapter 3:** the account of the SymPy Miller–Rabin issue is more precise.
- **Chapter 5:** the Chapter 5 epigraph (Bram Stoker, *Dracula*) uses a different passage, and the SHA-256 collision exercise says exactly what counts as a collision.
- **Chapter 7:** the key and signatures of Exercise 7.4 are available as [exercise_7_4_data.py](Chapter_7/exercise_7_4_data.py) in this repository.
- **Chapter 8:** Remark 8.1 explains how xⁿ + 1 factors modulo q and why that enables the Number Theoretic Transform.
- **Chapter 9:** a footnote in §9.2 lists every term of the decapsulation noise; §9.3.1 gives the average SHAKE-128 output consumed per entry of A (about 473 bytes) and notes that FIPS 203 calls this step SampleNTT.
- **Chapter 10:** Exercise 10.5 explains the shift z and how it differs from the signature vector z; §10.4.2 shows why Bob recovers Alice’s w₁; new footnotes describe the message prefix M′ and the two extra rejection checks of FIPS 204; §10.5.2 gives the average SHAKE-128 output per entry of A (about 769 bytes); the solution to Exercise 10.8 explains that ML-DSA and RSA run on different providers (Bouncy Castle and SunRsaSign).
- **Chapter 11:** the epigraph includes the original Nahuatl text of Nezahualcóyotl’s poem.
- **Preface:** Claude is added to the language models consulted.
- **Throughout:** punctuation, hyphenation and math typesetting were made consistent, and the index was revised.
