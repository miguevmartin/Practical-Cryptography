cipher = Cipher(algorithms.AES(sk), modes.ECB(), backend=backend)
decryptor2 = cipher.decryptor()
p=decryptor2.update(c)
decryptor2.finalize()
print('p:', p) # b'Oh wow! * three!'
