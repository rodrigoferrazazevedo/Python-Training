import hashlib
import os

print("Hash algorithms available: ", end="")
print(hashlib.algorithms_available)

print("")

h = hashlib.blake2b()
h.update(b'Hash me')
h.update(b' now!')

print("Blake2b hexdigest: ", end="")
print(h.hexdigest())

print("Blake2b digest: ", end="")
print(h.digest())

print("Block size: ", end="")
print(h.block_size)

print("Digest size: ", end="")
print(h.digest_size)

print("Algorithm name: ", end="")
print(h.name)

print("")

print("Blake2b hexdigest alternative: ", end="")
print(hashlib.blake2b(b'Hash me now!').hexdigest())

print("Blake2b digest alternative: ", end="")
print(hashlib.blake2b(b'Hash me now!').digest())

print("")

print("Blake2b hexdigest customized: ", end="")
print(hashlib.blake2b(b'Important payload', digest_size=16, key=b'secret-key', salt=b'random-salt', person=b'rodrigo').hexdigest())
print("Blake2b digest customized: ", end="")
print(hashlib.blake2b(b'Important payload', digest_size=16, key=b'secret-key', salt=b'random-salt', person=b'rodrigo').digest())

print("pbkdf2_hmac: ", end="")
dk = hashlib.pbkdf2_hmac('sha256', b'Password123', os.urandom(16), 100000)
print(dk.hex())