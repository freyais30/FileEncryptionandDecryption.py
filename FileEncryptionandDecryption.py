def encrypt_file(filename, key):
    with open(filename, 'rb') as f:
        data = f.read()
    encrypted_data = bytearray(data)
    for i in range(len(data)):
        encrypted_data[i] ^= key
    with open(filename, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(filename, key):
    encrypt_file(filename, key)

filename = input("Enter filename to encrypt/decrypt: ")
key = int(input("Enter encryption/decryption key: "))
decrypt_file(filename, key)
