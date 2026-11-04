h=b'\xb7\xd2v~w\xd4=\x86\xef\xf7\x84sv\xb0\xc7\x16'
y=b'imagin'
for _ in range (2**32):
    y1 = y + os.urandom(2)
    digest = hashes.Hash(hashes.MD5(), backend=default_backend())
    digest.update(y1)
    h1 = digest.finalize()
    if h1 == h:
        print(y1) #b'imagine+'
        print(f"found in {_} attempts")
        break
