### CIS-30C PYTHON FOR CYSEC -- Kasey Nguyen ###

# UNIT 1 Lab  -- 1:23:30

# Identify a package that can be used for Python security. Provide description and information 
# about the package and modules 

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# Define the key and initialization vector (IV)
key = b'ThisIsASecretKey'
iv = os.urandom(16) #generate a random 16-byte IV

# Create the cipher object
cipher = AES.new(key, AES.MODE_CBC, iv)

# Define the message to encrypt
message = b'This is a secret message'

# Pad the message to a multiple of 16 bytes using PKCS#7 padding
padded_message = pad(message, AES.block_size)

# Print padded message
print("padded message: ", padded_message)
print()

# Encrypt the message
encrypted_message = cipher.encrypt(padded_message)

# Print the encrypted message
print("Encrypted Message:", encrypted_message)
print()

# Create a new cipher object for decryption
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)

# Print the decrypted message
print("Decrypted Message:", decrypted_message)
print()

# Unpad the decrypted message
unpadded_message = unpad(decrypted_message, AES.block_size)

# Print the unpadded message
print("Unpadded Message:", unpadded_message)
print()

# Print the decrypted message
print("Decoded Message:", unpadded_message.decode())