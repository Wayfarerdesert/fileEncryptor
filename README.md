# Infector

This Python script encrypts files in the directory where it is placed, excluding itself (`infector.py`), the `decrypt.py` script, and the `decrypt.key` file. It utilizes the cryptography library to encrypt files and generates a unique key stored in `decrypt.key`.

## Usage

1. Make sure you have Python 3 installed on your system.
2. Place the `infector.py` script in the directory containing the files you want to encrypt.
3. Run the `infector.py` script.
4. All files in the directory (except `infector.py`, `decrypt.py`, and `decrypt.key`) will be encrypted using a unique key.
5. A file named `decrypt.key` containing the encryption key will be generated in the directory.
6. You will receive instructions on how to decrypt your files.

## Note

- **Important**: Do not lose the `decrypt.key` file. It is required for decryption and is unique to your set of encrypted files.
- Follow the instructions provided upon encryption to ensure proper decryption of your files.

# Decryptor

This Python script is designed to decrypt files that have been encrypted using the `infector.py` script. It utilizes the cryptography library to decrypt files using a secret key stored in a file named `decrypt.key`.

## Usage

1. Make sure you have Python 3 installed on your system.
2. Place the `decryptor.py` script in the directory containing the encrypted files.
3. Run the `decryptor.py` script.
4. You will be prompted to enter the decryption password.
5. If the password is correct, the script will decrypt all the files in the directory.
6. Congratulations, your files have been successfully decrypted!

## Note

- Make sure to keep the `decrypt.key` file safe and secure. It contains the secret key needed for decryption.
- Ensure that you remember the decryption password. Without it, you won't be able to decrypt your files.



