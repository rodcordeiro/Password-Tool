"""Testing an In-House Encryption Algorithm"""
import random
key = "hello jim"
default_length=200 # The Default Number of Characters in the Password
key = list(key) # Turn the Key into a list
print(f"Key: {key}")

"""Start Encrypt the Values"""
for index in range(0, 201):
    try:
        key[index] = ord(key[index])
    except IndexError:
        if index - len(key) == 1:
            key.append("end")
        else:
            key.append(random.randrange(1, 10000))
print(f"Encrypted Key: {key}")
new = []
"""Decrypt the Encrypted Key"""
for index in range(0, 201):
    if chr(key[index]) == "end":
        key = new
        break
    else:
        new.append(chr(key[index]))
print(f"Decrypted Key: {key}")