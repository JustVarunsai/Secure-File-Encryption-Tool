import os
from cryptography.fernet import Fernet
from pathlib import Path

class SecureFileHandler:
    def __init__(self, key=None):
        """Initialize the encryption handler with an optional key."""
        if key:
            self.key = key
        else:
            self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
    
    def save_key(self, key_file):
        """Save the encryption key to a file for later use."""
        with open(key_file, 'wb') as keyfile:
            keyfile.write(self.key)
    
    @staticmethod
    def load_key(key_file):
        """Load the encryption key from a file."""
        try:
            with open(key_file, 'rb') as keyfile:
                return keyfile.read()
        except FileNotFoundError:
            print(f"Error: Key file '{key_file}' not found.")
            return None
    
    def encrypt_file(self, file_path):
        """Encrypt a file using Fernet symmetric encryption."""
        try:
            with open(file_path, 'rb') as file:
                file_data = file.read()
            
            encrypted_data = self.cipher_suite.encrypt(file_data)
            encrypted_file_path = f"{file_path}.encrypted"
            
            with open(encrypted_file_path, 'wb') as file:
                file.write(encrypted_data)
            
            print(f"File encrypted successfully: {encrypted_file_path}")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
    
    def decrypt_file(self, encrypted_file_path):
        """Decrypt a previously encrypted file."""
        try:
            with open(encrypted_file_path, 'rb') as file:
                encrypted_data = file.read()
            
            decrypted_data = self.cipher_suite.decrypt(encrypted_data)
            decrypted_file_path = encrypted_file_path.replace('.encrypted', '.decrypted')
            
            with open(decrypted_file_path, 'wb') as file:
                file.write(decrypted_data)
            
            print(f"File decrypted successfully: {decrypted_file_path}")
        except FileNotFoundError:
            print(f"Error: File '{encrypted_file_path}' not found.")
        except Exception as e:
            print(f"Error decrypting file: {e}")

def main():
    
    file_handler = SecureFileHandler()

    # Optionally, save the key to a file
    # file_handler.save_key("encryption.key")

    # Load the key if needed
    # key = SecureFileHandler.load_key("encryption.key")
    # file_handler = SecureFileHandler(key=key)

    # Example of encrypting and decrypting a file
    file_path = input("Enter the path of the file to encrypt: ")
    file_handler.encrypt_file(file_path)

    encrypted_file_path = file_path + ".encrypted"
    file_handler.decrypt_file(encrypted_file_path)

if __name__ == "__main__":
    main()

#Made by Varunsai
