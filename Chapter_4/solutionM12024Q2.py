k = b'abcdefghijklmnop'
iv = b'0123456789abcdef'
ms = [modes.ECB(), modes.CFB(iv), modes.OFB(iv), modes.CTR(iv)]
p1 = b'a secret message'
p2 = b'a secret lessage'
for m in ms:
    cipher1 = Cipher(algorithms.AES(k), m, backend=backend)
    encryptor1 = cipher1.encryptor()
    c1 = encryptor1.update(p1)
    encryptor1.finalize()
    encryptor2 = cipher1.encryptor()
    c2 = encryptor2.update(p2)
    encryptor2.finalize()
    print(hamming(c1,c2)) #output is: 69 1 1 1
