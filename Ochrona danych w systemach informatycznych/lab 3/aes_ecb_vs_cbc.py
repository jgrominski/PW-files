import sys
from math import log2

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def calculate_entropy(text):
    entropy = 0
    for i in range(256):
        p = text.count(chr(i)) / len(text)
        if p != 0:
            entropy -= p * log2(p)
    return entropy


f = open(sys.argv[1], "r")
text = f.read()

key = sys.argv[2]

aes = AES.new(str.encode(key), AES.MODE_ECB)
ecb = aes.encrypt(str.encode(text))

iv = get_random_bytes(16)
aes = AES.new(str.encode(key), AES.MODE_CBC, iv)
cbc = aes.encrypt(str.encode(text))

print("Entropy of plain text: " + str(calculate_entropy(text)))
print("Entropy of ECB: " + str(calculate_entropy(ecb.decode("latin-1"))))
print("Entropy of CBC: " + str(calculate_entropy(cbc.decode("latin-1"))))
