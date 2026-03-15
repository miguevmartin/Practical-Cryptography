from cryptography.hazmat.primitives import hashes
digest = hashes.Hash(hashes.SHA3_512())
data = b"Long live PQC!"
digest.update(data)
hash_bytes = digest.finalize()
print(hash_bytes)
