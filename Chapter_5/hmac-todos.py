"""
Hashing, HMAC, and Digital Signatures — Timing and Functional Comparison

Last modified: February 2026
Author: Original code by Miguel Vargas Martin. TODOs added by ChatGPT

This program demonstrates:
1) A cryptographic hash (SHA-256)
2) A keyed MAC (HMAC-SHA-256)
3) A digital signature (DSA)

We compare:
- Functionality
- Verification behavior
- Rough execution time

⚠️ Timing values are illustrative only.
⚠️ DSA-1024 is used for demonstration purposes (not recommended today).
"""

# Helper: Load message from file
def getMessage():
    """
    Reads a binary file and returns its contents.

    Used to simulate hashing/authenticating a realistic-sized file
    (~5 MB PowerPoint in this example).
    """
    try:
        # TODO 1:
        # Modify the program so that the filename is read from input().
        # Ensure binary mode is preserved.

        infile = open('large_file.pptx', 'rb') # large_file should be "large"
        message = infile.read()
        infile.close()
        return message

    except:
        print('An error occurred')
        return b'None'


# Part 1 — Cryptographic Hash (SHA-256)

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
import time

# Create SHA-256 hash object
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())

digest.update(getMessage())

# Measure only finalization time (not update time)
t1 = time.time()
hash_value = digest.finalize()
t2 = time.time()

print('Hash computation takes {} seconds'.format(t2 - t1))

# TODO 2:
# Measure the time for BOTH update() and finalize().
# Compare total hashing time with MAC and signature times.

# Part 2 — HMAC (Keyed Message Authentication Code)

# 32-byte (256-bit) symmetric key
# ⚠️ Hardcoded for reproducibility — NEVER hardcode keys in real systems.
key = b'12345678' * 4  # TODO 3: Replace with os.urandom(32)

h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
h.update(getMessage())

t1 = time.time()
mac = h.finalize()
t2 = time.time()
print('MAC generation takes {} seconds'.format(t2 - t1))

# HMAC Verification
h1 = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
h1.update(getMessage())

t1 = time.time()
h1.verify(mac)   # Raises exception if verification fails
t2 = time.time()

print('MAC verification takes {} seconds'.format(t2 - t1))

# TODO 4:
# Modify one byte of the message and observe what happens during verification.
# Explain why HMAC verification must be constant-time.

# Part 3 — Digital Signature (DSA)
from cryptography.hazmat.primitives.asymmetric import dsa

# Generate DSA private key
# ⚠️ 1024-bit DSA is obsolete for production use.
private_key = dsa.generate_private_key(
    key_size=1024,
    backend=default_backend()
)
data = b"this is some data I'd like to sign"

# Sign the data (internally hashes using SHA-256)
signature = private_key.sign(
    data,
    hashes.SHA256()
)

# Obtain public key for verification
public_key = private_key.public_key()

# Verify signature
public_key.verify(
    signature,
    data,
    hashes.SHA256()
)

# TODO 5:
# Measure the time required for:
#   - Key generation
#   - Signing
#   - Verification
# Compare these times to hash and HMAC.
# Explain why digital signatures are significantly slower.

# TODO 6:
# Replace DSA with RSA or ECDSA and compare:
#   - Key sizes
#   - Signature sizes
#   - Performance
#   - Security levels

# TODO 7:
# Explain conceptually:
#   - Why a hash alone does NOT provide authentication
#   - Why HMAC provides integrity + authentication
#   - Why digital signatures provide non-repudiation
