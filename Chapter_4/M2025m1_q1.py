# -*- coding: utf-8 -*-
"""
AES and Stream Cipher Performance Comparison

Last modified: February 2026
Author: Prof. Miguel Vargas Martin

This program benchmarks the encryption and decryption time of several
block cipher modes (AES) and stream ciphers (RC4, ChaCha20).

⚠️ IMPORTANT:
- Timing results are implementation- and hardware-dependent.
- This code is for educational and comparative purposes only.
- Several constructions shown here (ECB, RC4) are cryptographically insecure
  and MUST NOT be used in real systems.
"""

import os, time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.decrepit.ciphers import algorithms as decrepit_algs

def getPlaintext():
    """
    Reads a binary file and returns its contents as plaintext.

    We use a moderately large file (~5 MB) to make timing differences
    between cipher modes observable.

    Returns:
        bytes: plaintext message, or b'None' on error
    """
    try:
        # print('File name:', end=' '); infile = open(input(), 'rb')
        # OR, instructors may replace this file with any sufficiently large binary
        infile = open('large_file.pptx', 'rb') # large_file should be large (e.g., > 5 MB)
        message = infile.read()
        infile.close()
        return message
    except:
        print('An error occured')
        return b'None'

# Cryptographic backend abstraction (OpenSSL underneath)
backend = default_backend()

# 256-bit AES key (hard-coded for reproducibility; DO NOT do this in practice)
k = b'abcdefghijklmnop'*2

# Random 128-bit IV (used by most AES modes)
iv = os.urandom(16)

# List of AES modes to benchmark
# Note: ECB is included strictly for comparison and pedagogical reasons
ms = [modes.ECB(), modes.CBC(iv), modes.CFB(iv), modes.CFB8(iv), modes.OFB(iv), modes.CTR(iv), modes.GCM(iv)]

message = getPlaintext()
print('mode\t\ttime' + '\t\t\t')

for m in ms:
    # PKCS#7 padding is required for block modes operating on arbitrary-length data
    padder = padding.PKCS7(128).padder()

    cipher1 = Cipher(algorithms.AES(k), m, backend=backend)

    # Encryption:
    encryptor1 = cipher1.encryptor()
    plaintext = padder.update(message)
    plaintext += padder.finalize()
    t1 = time.perf_counter()
    ct1 = encryptor1.update(plaintext)
    t2 = time.perf_counter() 
    encryptor1.finalize() 

    print('{} enc\t\t{:.3f} ms'.format(m.name, 1000*(t2-t1)))
    
    # Decryption:
    # GCM requires special handling due to authentication tags
    if(m.name != "GCM"):
        decryptor1 = cipher1.decryptor()
        t1 = time.perf_counter() 
        pt1 = decryptor1.update(ct1) 
        t2 = time.perf_counter() 
        decryptor1.finalize() 
        print('{} dec\t\t{:.3f} ms'.format(m.name, 1000*(t2-t1)))
    else:
        # GCM decryption requires the authentication tag generated at encryption
        tag = encryptor1.tag
        cipher1 = Cipher(algorithms.AES(k), modes.GCM(iv, tag), backend=backend)
        decryptor1 = cipher1.decryptor()
        t1 = time.perf_counter()
        decryptor1.authenticate_additional_data(b"")
        pt1 = decryptor1.update(ct1) 
        t2 = time.perf_counter() 
        decryptor1.finalize() 
        print('{} dec\t\t{:.3f} ms'.format(m.name, 1000*(t2-t1)))

# Stream ciphers
# RC4 (deprecated and insecure, included for historical comparison)
cipher2 = Cipher(decrepit_algs.ARC4(k), mode=None, backend=backend)
encryptor2 = cipher2.encryptor()
t1 = time.perf_counter()
ct2 = encryptor2.update(plaintext)
t2 = time.perf_counter()
print('RC4 enc\t\t{:.3f} ms'.format(1000*(t2-t1)))

decryptor2 = cipher2.decryptor()
t1 = time.perf_counter()
ct2 = decryptor2.update(ct2)
t2 = time.perf_counter()
print('RC4 dec\t\t{:.3f} ms'.format(1000*(t2-t1)))

# ChaCha20 (modern stream cipher, designed to be fast in software)
cipher3 = Cipher(algorithms.ChaCha20(k,iv), mode=None)
encryptor3 = cipher3.encryptor()
t1 = time.perf_counter()
ct3 = encryptor3.update(plaintext)
t2 = time.perf_counter()
print('ChaCha20 enc {:.3f} ms'.format(1000*(t2-t1)))

decryptor3 = cipher3.decryptor()
t1 = time.perf_counter()
ct3 = decryptor3.update(ct3)
t2 = time.perf_counter()
print('ChaCha20 dec {:.3f} ms'.format(1000*(t2-t1)))

# AES-XTS (used for disk encryption)
k = b'0123456789abcdeffedcba9876543210'
sector = b'1234567800000000'
cipher4 = Cipher(algorithms.AES(k), modes.XTS(sector), backend=backend)
encryptor4 = cipher4.encryptor()
t1 = time.perf_counter()
ct4 = encryptor4.update(plaintext)
t2 = time.perf_counter()
print('XTS enc\t\t {:.3f} ms'.format(1000*(t2-t1)))

decryptor4 = cipher4.decryptor()
t1 = time.perf_counter()
ct4 = decryptor4.update(ct4)
t2 = time.perf_counter()
print('XTS dec\t\t {:.3f} ms'.format(1000*(t2-t1)))

# Part d)a.
''' 
mode		time
ECB enc		2.278 ms
ECB dec		4.026 ms
enc is generally faster.
This is in part due to encryption and decryption not being the same algorithm.
But most importantly, keep in mind that the matrix used in the MixColumns transformation is optimized for encryption, not for decryption.

CBC enc		5.258 ms
CBC dec		2.340 ms
dec is generally faster.
Note that unlike encryption, decryption can be parallelized.

CFB enc		6.957 ms
CFB dec		6.900 ms
dec is generally faster.
Decryption can be parallelized, encryption cannot.

CFB8 enc		91.941 ms
CFB8 dec		89.420 ms
dec is generally faster.
Idem (decryption can be parallelized, encryption cannot.)

OFB enc		5.579 ms
OFB dec		6.238 ms
After many obervations, there is not a clear winner because enc and dec are identical.

CTR enc		2.907 ms
CTR dec		2.576 ms
Idem.

GCM enc		2.846 ms
GCM dec		2.668 ms
Idem. 

RC4 enc		10.709 ms
RC4 dec		11.519 ms
Idem.

ChaCha20 enc 3.942 ms
ChaCha20 dec 3.326 ms
Idem.

XTS enc		 2.366 ms
XTS dec		 2.681 ms
enc is generally faster.
This is in part due to encryption and decryption not being the same algorithm.
But most importantly, keep in mind that the matrix used in the MixColumns transformation is optimized for encryption, not for decryption.
'''

# Part d)b
'''
From fastest to the slowest:
CBC dec		2.340 ms The power of parallelization!
CTR dec		2.576 ms CBC consistently beats CTR. This is most likely implementation-dependent.
GCM dec		2.668 ms GCM requires the GHASH calculation. 
XTS dec		 2.681 ms After a few observations, no clear winner between XTS and GCM.
ChaCha20 dec 3.326 ms If you run the code in a hardware-optimized AES machine, it is likely that AES will outperform non-AES algorithms.
ECB dec		4.026 ms The weakness of sequantiality.
OFB dec		6.238 ms OFB may be pre-computable but not parallelizable.
CFB dec		6.900 ms CFB may be parallelizable once ciphertext is available, but it is not pre-computable.
RC4 dec		11.519 ms If you run the code in a hardware-optimized AES machine, it is likely that AES will outperform non-AES algorithms.
CFB8 dec		89.420 ms CFB needs to process ~16x the number of blocks than other modes.
'''