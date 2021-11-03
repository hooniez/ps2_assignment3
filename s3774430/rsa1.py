import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)

publickey = key.publickey

encrypted = publickey.encrypt('encrypt this message', 32)

print('encrypted message:', encrypted)

f = open('encryption.txt', 'w')
f.write(str(encrypted))
f.close()

f = open('encryption.txt', 'r')
message = f.read()

decrypted = key.decrypt(message)

print('decrpyted', decrypted)

f = open('encryption.txt', 'w')
f.write(str(message))
f.write(str(decrypted))
