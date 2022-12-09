from random import randrange

from Crypto.PublicKey import RSA

key = RSA.generate(2048)

msg = randrange(2, 1000)
enc = pow(msg, key.e, key.n)
dec = pow(enc, key.d, key.n)

print("Message: " + str(msg) + "\nEncrypted: " +
      str(enc) + "\nDecrypted: " + str(dec))
