"""
RSA vs AES Performance and Key Serialization Demo

Last modified: February 2026
Author: Original code by Miguel Vargas Martin, TODOs by ChatGPT

This program demonstrates:

1) RSA key generation and serialization (PEM format)
2) RSA encryption using OAEP padding
3) AES symmetric encryption (OFB mode)
4) Basic hashing (MD5 example)
5) (Commented) RSA signature example

The goal is to compare:
- Public-key vs symmetric-key performance
- Proper padding schemes
- Key storage formats

⚠️ Educational purposes only.
⚠️ MD5 is cryptographically broken and included for demonstration.
"""

# Key Serialization Utilities
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend

def save_key(pk, filename, passw):
    """
    Serialize and store a private key in PEM format.

    Currently uses:
        - TraditionalOpenSSL format
        - No encryption (NoEncryption())

    ⚠️ The passw parameter is unused.
    TODO 1:
        Modify this function to encrypt the private key using:
            serialization.BestAvailableEncryption(passw)
        Explain why storing unencrypted private keys is dangerous.
    """
    pem = pk.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open(filename, 'wb') as pem_out:
        pem_out.write(pem)

def load_key(filename):
    """
    Load a PEM-encoded private key from disk.

    If the key is encrypted, a password must be supplied.
    """
    with open(filename, 'rb') as pem_in:
        pemlines = pem_in.read()

    private_key = load_pem_private_key(
        pemlines,
        password=None,
        backend=default_backend()
    )

    return private_key


# RSA Key Generation
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import time, os

backend = default_backend()

# Measure RSA key generation time
t0 = time.time()
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=backend
)
t1 = time.time()

# Save and reload private key
save_key(private_key, 'private_key.pem', b'yetanotherpassword')
public_key = load_key('private_key.pem').public_key()
# (Equivalent to: private_key.public_key())

print("RSA key generation time:", t1 - t0, "seconds")

# TODO 2:
# Measure how key generation time changes for:
#   - 1024-bit
#   - 3072-bit
#   - 4096-bit
# Explain why key generation time increases.

# RSA Encryption (OAEP)
message = b'secret message' * 14

t2 = time.time()
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA224()),
        algorithm=hashes.SHA224(),
        label=None
    )
)
t3 = time.time()

print('RSA-OAEP:',
      'key gen:', t1 - t0, 'sec,',
      'enc:', t3 - t2, 'sec')

# OAEP provides semantic security (IND-CPA).
# TODO 3:
# Replace SHA224 with SHA256 in OAEP.
# Explain why OAEP is necessary instead of "raw RSA".

# AES Symmetric Encryption
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# 256-bit AES key (hardcoded for reproducibility)
k = b'abcdefghijklmnop' * 2

iv = os.urandom(16)     # 128-bit IV
mode = modes.OFB(iv)    # OFB = stream-like block mode

cipher1 = Cipher(algorithms.AES(k), mode, backend=backend)
encryptor1 = cipher1.encryptor()

t1 = time.time()
ct1 = encryptor1.update(message)
t2 = time.time()
encryptor1.finalize()

print('AES-OFB encryption time:', t2 - t1, 'sec')

# TODO 4:
# Compare RSA encryption time with AES encryption time.
# Explain why symmetric encryption is dramatically faster.
# What does this imply about hybrid encryption schemes?

# Hash Example (MD5)
digest = hashes.Hash(hashes.MD5(), backend=default_backend())
digest.update(b"abc")
digest.update(b"123")
dg = digest.finalize()

# ⚠️ MD5 is collision-broken and should not be used for security.
# TODO 5:
# Replace MD5 with SHA256.
# Demonstrate how two different inputs can collide under MD5
# (research-based exercise).


# (Commented) RSA Signature Example
'''
signature = private_key.sign(
     message,
     padding.PSS(
         mgf=padding.MGF1(hashes.SHA256()),
         salt_length=padding.PSS.MAX_LENGTH
     ),
     hashes.SHA256()
 )
'''

# TODO 6:
# Uncomment the signature code and:
#   - Measure signing time
#   - Measure verification time
# Compare with encryption time.
# Why is signing typically slower than verification?
