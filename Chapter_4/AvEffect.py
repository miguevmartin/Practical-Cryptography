"""
Avalanche Effect Exploration using Triple DES (3DES)

This program illustrates how small changes in the key or plaintext
may (or may not!) affect the ciphertext, depending on the cipher
and mode of operation.

Last modified: February 2026
Author: Miguel Vargas Martin
"""

import warnings
warnings.filterwarnings('ignore')

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def hamming(a, b):
    """
    Compute the Hamming distance between two byte strings.

    The Hamming distance counts the number of bit positions
    in which two equal-length byte strings differ.

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


# Key setup
backend = default_backend()
# Two closely related 3DES keys (24 bytes each)
k1 = b'12345678' * 3
k2 = b'123456781234567812345679'

# Guiding questions:
# 1) If hamming(k1, k2) = 1, why is hamming(ct1, ct2) = 0?
#    (Hint: think about how 3DES keys are internally structured.)
# 2) Now set:
#       k2 = b'123456781234567812345677'
#    and observe that hamming(k1, k2) = 4. Why?
# 3) Exercise:
#    Find k1 and k2 such that:
#       hamming(k1, k2) = 1
#       hamming(ct1, ct2) > 0
#    Example attempt:
#    k1 = b'12345679' * 3
#    k2 = b'123456791234567912345479'

# Avalanche effect with respect to the key
cipher1 = Cipher(algorithms.TripleDES(k1), modes.ECB(), backend=backend)
cipher2 = Cipher(algorithms.TripleDES(k2), modes.ECB(), backend=backend)

encryptor1 = cipher1.encryptor()
encryptor2 = cipher2.encryptor()

# Same plaintext encrypted under two slightly different keys
ct1 = encryptor1.update(b"a secret message") + encryptor1.finalize()
ct2 = encryptor2.update(b"a secret message") + encryptor2.finalize()

print(
    'Avalanche effect (same plaintext, different keys):',
    hamming(ct1, ct2)
)

# Avalanche effect with respect to the plaintext
encryptor3 = cipher1.encryptor()
encryptor4 = cipher1.encryptor()

# Two plaintexts differing by a single bit:
#   hamming(b'a secret', b'a secreu') = 1
ct3 = encryptor3.update(b"a secret") + encryptor3.finalize()
ct4 = encryptor4.update(b"a secreu") + encryptor4.finalize()

# Question:
# What happens if we instead use b"a secres"?
# Does the bit position of the change matter?

print(
    'Avalanche effect (different plaintexts, same key):',
    hamming(ct3, ct4)
)
