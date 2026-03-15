"""
RSA Encryption and Digital Signature Demo

Modified: February 2026
Author: Miguel Vargas Martin

This program demonstrates:

1) RSA key generation
2) Private key serialization (PEM format)
3) RSA encryption using OAEP padding
4) RSA digital signatures using PSS
5) Signature verification

⚠️ Educational demonstration only.
⚠️ Private key is stored without encryption (not secure in practice).
"""

# Key Serialization Utilities
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key

def save_key(pk, filename, passw):
    """
    Save a private RSA key to disk in PEM format.

    Current configuration:
        - TraditionalOpenSSL format
        - No encryption (NoEncryption())

    ⚠️ The 'passw' parameter is not used.
    ⚠️ Storing private keys without encryption is insecure.
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
    Load a private RSA key from a PEM file.
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

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

backend = default_backend()

# Generate a 2048-bit RSA key pair
# public_exponent=65537 is the standard secure choice
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=backend
)

# Save private key to disk
save_key(private_key, 'private_key.pem', b'yetanotherpassword')

# Extract public key from stored private key
# (Equivalent to private_key.public_key())
public_key = load_key('private_key.pem').public_key()

# RSA Encryption (Confidentiality)

message = b'secret message' * 2

# Encrypt using RSA-OAEP
# OAEP provides semantic security (IND-CPA)
# SHA224 is used here for both MGF1 and hash function
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA224()),
        algorithm=hashes.SHA224(),  # Possible: SHA1, 224, 256, 384, 512
        label=None
    )
)

# NOTE:
# - Raw RSA must never be used.
# - OAEP is required to prevent deterministic encryption attacks.

# RSA Digital Signature (Authenticity + Integrity)

signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# PSS is the recommended modern signature padding.
# It provides provable security in the random oracle model.

# Signature Verification

# Recreate message (for clarity)
message = b'secret message' * 2

# Verify signature using the public key
# If verification fails, an exception is raised.
public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# If no exception is raised, the signature is valid.

# Security Notes
"""
1) Encryption vs Signature:

   - Encryption uses the PUBLIC key.
   - Signing uses the PRIVATE key.
   - Verification uses the PUBLIC key.

2) OAEP vs PSS:

   - OAEP → used for encryption.
   - PSS  → used for digital signatures.

3) Hash choices:

   - SHA256 is recommended.
   - SHA1 is deprecated.
   - SHA224 is acceptable but less common than SHA256.

4) Private Key Storage:

   - This example stores the private key without encryption.
   - In practice, always use:
         serialization.BestAvailableEncryption(password)

5) RSA is slow compared to symmetric encryption.
   In real systems, hybrid encryption is used:
        RSA encrypts an AES key,
        AES encrypts the data.
"""
