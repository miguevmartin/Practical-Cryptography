"""
Avalanche Effect Exploration using AES

This exercise mirrors the earlier 3DES experiment, but now uses AES.
Students are encouraged to compare the avalanche behavior of modern
block ciphers under similar conditions.

Last modified: February 2026
Author: Miguel Vargas Martin
"""

import warnings
warnings.filterwarnings('ignore')

import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def hamming(a, b):
    """
    Compute the Hamming distance (bitwise) between two byte strings.

    Parameters
    ----------
    a, b : bytes
        Byte strings of equal length.

    Returns
    -------
    int
        Number of differing bits.
    """
    return bin(
        int.from_bytes(a, 'big') ^ int.from_bytes(b, 'big')
    ).count('1')

# AES setup
backend = default_backend()

# AES keys (128-bit)
# Exercise (b): try 192-bit and 256-bit keys
k1 = b'12345678' * 2                 # 16 bytes
k2 = b'1234567812345679'             # differs by one bit

# Initialization Vector (CBC mode requires a random IV in practice)
iv = b'fedcba9876543210'              # 16 bytes (AES block size)

# Plaintext must be a multiple of 16 bytes when using CBC with no padding
plaintext = b"a secret message"       # exactly 16 bytes

# Guiding questions:
# 1) If hamming(k1, k2) is small, do we always get a large
#    hamming(ct1, ct2)? Why or why not?
# 2) What changes if the IV is modified?
# 3) How does AES compare to 3DES in terms of avalanche behaviour?

# Avalanche effect: key difference
cipher1 = Cipher(algorithms.AES(k1), modes.CBC(iv), backend=backend)
cipher2 = Cipher(algorithms.AES(k2), modes.CBC(iv), backend=backend)

encryptor1 = cipher1.encryptor()
encryptor2 = cipher2.encryptor()

start = time.time()
ct1 = encryptor1.update(plaintext) + encryptor1.finalize()
end = time.time()

ct2 = encryptor2.update(plaintext) + encryptor2.finalize()

print(
    'Avalanche effect (same plaintext, different keys):',
    hamming(ct1, ct2)
)
print('Encryption time (single block): {:.6f}s'.format(end - start))

# Avalanche effect: plaintext difference
encryptor3 = cipher1.encryptor()
encryptor4 = cipher1.encryptor()

# These two plaintexts differ by a single bit
p1 = b'a secret message'
p2 = b'a secret messagd'

ct3 = encryptor3.update(p1) + encryptor3.finalize()
ct4 = encryptor4.update(p2) + encryptor4.finalize()

# Guiding question:
# Compare hamming(p1, p2) with hamming(ct3, ct4).
# Does AES exhibit a stronger avalanche effect than 3DES?

print(
    'Avalanche effect (different plaintexts, same key):',
    hamming(ct3, ct4)
)
