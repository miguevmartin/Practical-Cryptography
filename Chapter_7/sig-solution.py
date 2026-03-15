signature = base64.b64decode('NNB43...=')
public_key = serialization.load_pem_public_key(pem_bytes)
public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
#Answer: 3(ZGji),4(kvPY+),8(ZLMF5),9(Aes4f),10(NNB43)
