uk=aes_key_unwrap(wgk, wdk)
cipher = Cipher(algorithms.AES(uk), modes.ECB(), backend=default_backend())
decryptor2 = cipher.decryptor()
p=decryptor2.update(c) 
decryptor2.finalize()
print('p:', p) #  b'helpIneedSomebdy'
