from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(key, input_path, output_path):
    fernet = Fernet(key)
    with open(input_path, 'rb') as file:
        data = file.read()
    encrypted = fernet.encrypt(data)
    with open(output_path, 'wb') as file:
        file.write(encrypted)

def decrypt_file(key, input_path, output_path):
    fernet = Fernet(key)
    with open(input_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted = fernet.decrypt(encrypted_data)
    with open(output_path, 'wb') as file:
        file.write(decrypted)

