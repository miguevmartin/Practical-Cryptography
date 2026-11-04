y = b'dh$g.u'
for _ in range (2**32):
    y1 = y + os.urandom(2)
    digest = hashes.Hash(hashes.MD5(), backend=default_backend())
    digest.update(y1)
    h1 = digest.finalize()
    if h1 == h:
        print(y1) #b'dh$g.uj#'
        break
