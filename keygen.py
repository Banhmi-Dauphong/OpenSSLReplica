from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate a private RSA key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Save the private key to a file
with open("private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Generate the public key
public_key = private_key.public_key()

# Save the public key to a file
with open("public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))


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
