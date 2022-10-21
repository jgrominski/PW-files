from math import inf, log2
import sys
from Crypto.Cipher import ARC4

ARC4.key_size = range(3, 257)

def calculate_entropy(text):
    entropy = 0
    for i in range(256):
        p = text.count(chr(i)) / len(text)
        if p != 0:
            entropy -= p * log2(p)
    return entropy

f = open(sys.argv[1], "rb")
encrypted = f.read()

lowest_entropy = inf
lowest_entropy_key = "aaa"

for i in range(ord('a'), ord('z') + 1):
    for j in range(ord('a'), ord('z') + 1):
        for k in range(ord('a'), ord('z') + 1):
            key = chr(i) + chr(j) + chr(k)
            cipher = ARC4.new(str.encode(key))
            decrypted = cipher.decrypt(encrypted).decode("latin-1")
            entropy = calculate_entropy(decrypted)
            if entropy < lowest_entropy:
                lowest_entropy = entropy
                lowest_entropy_key = key

cipher = ARC4.new(str.encode(lowest_entropy_key))
decrypted = cipher.decrypt(encrypted).decode("latin-1")
print(decrypted)