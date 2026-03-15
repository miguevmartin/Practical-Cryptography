k = b'kdnc649snc04ajx'
for _ in range (2**16):
    kk = k + os.urandom(1)
    try:
        uk = aes_key_unwrap(kk,
b'\xa4\xe00\xdb\xfa\x02\x18\xaa\x85\xb2\x9db\xa3\xe2\x02\xea\xe2\xf3\x9d}\xa5\xa9\xba(',
                            backend=default_backend())
        print(uk) # b'ThanK You FolKs!'
        print(kk) # b'kdnc649snc04ajx&
        break
    except:
        continue
