# -*- coding: utf-8 -*-
"""
Brute-Forcing a Short AES-CMAC Key

Last modified: February 2026
Author: Miguel Vargas Martin

This program demonstrates why short keys are insecure,
even when used with strong primitives such as AES-CMAC.

We:
  1) Compute a valid CMAC tag using a full 128-bit AES key.
  2) Assume that only part of the key is known.
  3) Brute-force the remaining unknown bits.
  4) Recover the correct key by verifying the MAC.

⚠️ Educational purpose only.
⚠️ Real systems must NEVER use short or partially secret keys.
"""

from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms
import os

# Let's compute the tag, instead of copying it from the exercise's text

# 16-byte (128-bit) AES key
key = b'0123456789abcdi/'  

message = b"message to authenticate"

# Create CMAC object using AES
c = cmac.CMAC(algorithms.AES(key))
c.update(message)

# Generate authentication tag
tag = c.finalize()

print("Valid tag:", tag) #b's\xaf\x12\n\xdc\xc6\x16~\xd0\xcaI\xf3o\x9au0'

# Now let's assume we are missing the last 2 bytes (16 bits) of the key

key = b'0123456789abcd'   # 14 known bytes, last 2 are unknown

# Total search space: 2^16 possible values
# (We loop slightly larger here: 2^17 attempts)
for _ in range(2**17):

    # Guess the missing 2 bytes
    key1 = key + os.urandom(2)

    try:
        # Compute CMAC under guessed key
        c = cmac.CMAC(algorithms.AES(key1))
        c.update(message)

        # Check whether computed tag matches the known valid tag
        c.verify(tag)

        # If verification succeeds, we have found the correct key
        print("Recovered key:", key1) # b'0123456789abcdi/'
        break

    except:
        # Verification failed → wrong key guess
        continue
