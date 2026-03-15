def xor(a, b):
    return (int.from_bytes(a,'big')^int.from_bytes(b,'big')).to_bytes(32,byteorder='big')

digest = hashes.Hash(hashes.SHA256())
digest.update(cv)
h=digest.finalize()
K=xor(h,mk)

cipher = Cipher(algorithms.AES(K), modes.ECB(), backend=backend)
decryptor = cipher.decryptor()
sk=decryptor.update(esk)
decryptor.finalize()
print('sk:', sk) # b'secretKey-a3d8fg'
