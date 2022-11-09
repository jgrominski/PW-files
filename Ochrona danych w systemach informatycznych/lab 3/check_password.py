import itertools
import sys
from math import log2

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


def calculate_password_entropy(text):
    alphabet_size = 0
    small_chars = range(ord('a'), ord('z') + 1)
    big_chars = range(ord('A'), ord('Z') + 1)
    numbers = range(ord('0'), ord('9') + 1)

    if any(chr(c) in text for c in small_chars):
        alphabet_size += 26
    if any(chr(c) in text for c in big_chars):
        alphabet_size += 26
    if any(chr(c) in text for c in numbers):
        alphabet_size += 10
    if any(ord(c) not in itertools.chain(small_chars, big_chars, numbers) for c in text):
        alphabet_size += 194

    return len(text) * log2(alphabet_size)


f = open(sys.argv[1], "r")
text = f.read()

password = sys.argv[3]
password_entropy = calculate_password_entropy(password)

if password_entropy < 100:
    print("Password entropy is lower than 100 bits: " +
          str(round(password_entropy, 2)))
else:
    print("Password entropy is greater than 100 bits: " +
          str(round(password_entropy, 2)))

salt = get_random_bytes(16)
key = PBKDF2(str.encode(password), salt, dkLen=16)

iv = get_random_bytes(16)
aes = AES.new(key, AES.MODE_CBC, iv)
encrypted = aes.encrypt(str.encode(text))

out = open(sys.argv[2], "wb")
out.write(encrypted)
out.close()
