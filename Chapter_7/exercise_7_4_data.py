"""
Data for Exercise 7.4 (RSA-PSS signature verification).

The message, the public key in PEM format and the ten Base64 signatures,
exactly as printed in the book, so they do not have to be retyped.
Import them in your solution, for example:

    from exercise_7_4_data import message, pem_bytes, signatures

Last modified: November 2026
Author: Miguel Vargas Martin
"""

message = b'A heartfelt thank you to Galois and Fermat!'

pem_bytes = (
    b'-----BEGIN PUBLIC KEY-----\n'
    b'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCpeGfrPlftac6CbipqMFde1YMm\n'
    b'T8dPyosJ742KeZMeUqTDO5BsOV6Un5Ab8tM5o6VEVumOsg4D6rTO6HhCpouzXchV\n'
    b'a38fOgKwQ5t9HblTCLM3C/3brOJ1mGGeOUQAAElK7NzoMlufJFKChCOg5VkuyjJX\n'
    b'1iYn5aOcbVAXiAsQgwIDAQAB\n'
    b'-----END PUBLIC KEY-----\n'
)

signatures = [
    'PvfyQ0IXkl4TOqrHv+noDGV5X9MN0cxBScVJBFbBE30FSmkqP6dJ/1SxWdhE8xKdjy02lDLTZgHGGuhtPG0Rr73fEJlkqoUgs3uLfiIPCWzriy6Ebuen9yQ7X4qlVQF8SfcROkW5KUgGe28lYT0StiUlQLdyQfbpJtU4spasQDQ=',  # Signature 1
    'gqp9EaLFVeBJRKO6+kUW5yiknsI1t2pL+FecagZWKxNOu6GgLnJTT8ntcbLfAY7db2iB74YK0eo6C0r2VRXBvbivQGMRRG5xSiFIYpKZ2YwLDOjYbCcb4ioRwyFijzbugLvNFUDbSGtA7DeZvlYiG8uZa9n0bxyQtcvHlUdHinY=',  # Signature 2
    'ZGjiYA9Ic4bl6ccxDtbGeGWh+Lv2xoVizxdPwi/7boKihbONU+g8kYBZOyP3vjr1xB/55BZuC8B9x2ONlyrcqS4U+7Za7G8ik8WYGXn+sSqQugrM94Cbbw8HV/LQdDkkzWX3XmV0GNQ+ZQ5fAwmnMtpboT0Bod9WbObi90LRTQc=',  # Signature 3
    'kvPY+Q07oim687QqcP2erEOFa+eR9TWxRN4Aa0QjJkn+ZfmaFUtZGf13o4btdz+lHXTTigpFSC38s0IhH+tM5JzSLGl8NscOkQi0BGnQz06tCK66fh7I2jafv4gE4HrqDDcrLhMtXbtjlGe3yESTSAWgCTDp4V6FTIDAyTCltpk=',  # Signature 4
    'a+gE2Rw4VgNWBbt2M1++9l6ilivB9utX6Bv6TPADAzZwR1mtQXwqXPX8Ov0fqKsO/w0ENcWwvz8Tplt9HtTBRw4ksEXrZTW/7f6hsVmHdryyRB0iOozVSyn522UIU8CaN8PDGWzAWp7GKwiFuvz6G2OYwAkd92IfzgvMH6yQPrI=',  # Signature 5
    'ZC6COa99eLTchMESpki2mgtJx3/L/1yCAQyOlY3mkznB3+EM+bQgLhRy9q7Nky5221PHmmA80Zaeg4gz3b1qY8RqYNIY2eS8jeUP4XcUervw4hmq2bIhrb/3YRGglujGldwmhwzENEcHRBOmUivJI5JFfoFW4QlfMSIVkiSNndw=',  # Signature 6
    'M9ll5wk2lsKtzwkqij+TJFO6cu8avIe0tx3iy10t45U9MQAA/ziog7qBFbmkgdFq2h6mKGyFCpCkEaPel9Mj8yvRoDTwVDKhWPaeJh0dFW7EbK53LCFqSDiAr/4xSc2gsLX1OlVlF6Lf6TOAQgATznOXGMWr6nc78Y1ret0TF00=',  # Signature 7
    'ZLMF5sM2RaraKnRbU2XNoaOKXqhimaPSsWbqZhMpk4KnOXQhCbRlBWE2WgSMr1OxJDVnfszLGVLy/N+PhprVuD9XTqX0VMNdcK3YYsx4F/MB0jNR2NSB0XYGim0A4zCJIqvDk6EOOoBvf5ZnKEsUh9bdCJhdTqmP8uA6RIke7WQ=',  # Signature 8
    'Aes4f/Rm/WXlv9WVSwf+nlRYi+TC/bTfKy0NXOXBtdXEiQtN8JHHpRWJ1iHtAa3D4v907rmHy+vdTgeBe3EItEJT5WyrKDTVTgKS+EA+2OPFtkuJcbzwOvnd3FpV47wGFFR1uOPmR6RzZ5+ZySMDZ21+6eGALWMfNjJxEwJYj/8=',  # Signature 9
    'NNB43VvC3MW8qwRxdA1NR+556OSV4lU5PBNnKlTU6kuSSUTOy3GUHqU60M24zehWWnEjwnq4XcfTudmwkPwm7TF0C11cfy1eAsUuWeWRjeC/DtU8byPoRj7M1bHSAunSXLPMvrTKVvb8gCbbcSudJ/ZYrTow3l14LUUgUjFuvwk=',  # Signature 10
]
