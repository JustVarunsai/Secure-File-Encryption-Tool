# SecureFileEncryptor

SecureFileEncryptor is a Python-based file encryption and decryption tool that ensures the confidentiality of your sensitive data using **Fernet** symmetric encryption from the **cryptography** library. This tool provides simple yet effective encryption and decryption for any file, and supports key management for secure storage and retrieval.

## Features

- **File Encryption**: Encrypt files with symmetric encryption using a generated or provided key.
- **File Decryption**: Decrypt previously encrypted files with the corresponding key.
- **Key Management**: Option to save and load encryption keys for reuse in future sessions.
- **Error Handling**: Handles missing files, incorrect paths, and decryption errors with informative messages.

## Installation

To get started with the project, you need to install the required dependencies.

1. Clone the repository:
    ```bash
    git clone https://github.com/JustVarunsai/SecureFileEncryptor.git
    cd SecureFileEncryptor
    ```

2. Install the dependencies:
    ```bash
    pip install cryptography
    ```

## Usage

### Encrypting a File

1. To encrypt a file, run the script and input the file path when prompted:
    ```bash
    python secure_file_handler.py
    ```
2. The script will ask for the path of the file you want to encrypt. Once entered, the file will be encrypted and saved with an `.encrypted` extension.

### Decrypting an Encrypted File

1. After encryption, you can decrypt the file by entering the path of the `.encrypted` file when prompted:
    ```bash
    python secure_file_handler.py
    ```
2. The script will decrypt the file and save it with a `.decrypted` extension.

### Key Management

- **Save Key**: You can save the encryption key to a file for later use with the `save_key()` method.
- **Load Key**: If you have an existing key, you can load it using the `load_key()` method.

## Example

```python
# Encrypt a file
file_handler = SecureFileHandler()
file_handler.encrypt_file('example.txt')

# Decrypt the encrypted file
file_handler.decrypt_file('example.txt.encrypted')
