from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Reading private key
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

# Reading public key
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

# Getting private key's component
private_numbers = private_key.private_numbers()

print("Private Key Components:")
print("Public Exponent:", private_numbers.public_numbers.e)
print("Modulus:", private_numbers.public_numbers.n)
print("Private Exponent:", private_numbers.d)
print("Prime 1:", private_numbers.p)
print("Prime 2:", private_numbers.q)
print("Exponent 1:", private_numbers.dmp1)
print("Exponent 2:", private_numbers.dmq1)
print("Coefficient:", private_numbers.iqmp)

# Getting public key's component
public_numbers = public_key.public_numbers()

print("\nPublic Key Components:")
print("Public Exponent:", public_numbers.e)
print("Modulus:", public_numbers.n)
