keys = [b'4k15coLr',b'5j04boMsyoswyi3pyoswyi3p',b'c5hzpd4lc5hzpd4l4k15cnMs']
iv = b'hicrypto'
mode = modes.CFB(iv)
message = b'But the soup is getting cold'
for k in keys:
    padder = padding.PKCS7(64).padder()
    cipher1 = Cipher(algorithms.TripleDES(k), mode, backend=backend)
    encryptor1 = cipher1.encryptor()
    plaintext = padder.update(message)
    plaintext += padder.finalize()
    ct1 = encryptor1.update(plaintext)
    encryptor1.finalize()
    print('k='+str(k)+':')
        print(ct1) # b'\x85...\x90\xb3\xbd&N_X\xc3\xc6=aT\x13\x93\xef\xcb\x99'
