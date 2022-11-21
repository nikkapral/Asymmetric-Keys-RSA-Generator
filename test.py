from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.exportKey()
file = open("private.pem","wb")
file.write(private_key)
file.close()

public_key = key.public_key().export_key()
file = open("public.pem", "wb")
file.write(public_key)
file.close()

