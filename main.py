import os

def decrypt_files() -> None:
    """Decrypts all files in a given directory that have been encrypted using a simple XOR encryption algorithm."""
    directory_path: str = input("Enter the directory path: ")
    decryption_key: str = input("Enter the decryption key: ")

    key_length: int = len(decryption_key)
    for filename in os.listdir(directory_path):
        # We only decrypt files that have the '.crypt' extension
        if filename.endswith(".crypt"):
            encrypted_file_path: str = os.path.join(directory_path, filename)
            decrypted_file_path: str = os.path.join(directory_path, encrypted_file_path[:-6])  # Remove '.crypt' extension

            # We read the encrypted file and XOR each byte with the corresponding byte in the decryption key
            with open(encrypted_file_path, "rb") as encrypted_file:
                decrypted_content: bytes = bytes([byte ^ ord(decryption_key[i % key_length]) for i, byte in enumerate(encrypted_file.read())])

            # We write the decrypted content to a new file and remove the encrypted file
            with open(decrypted_file_path, "wb") as decrypted_file:
                decrypted_file.write(decrypted_content)

            os.remove(encrypted_file_path)

def main():
    try:
        decrypt_files()
        print("Decryption successful.") 
    except Exception as e:
        print(f"Decryption failed: {e}")
    finally:
        print("Exiting...")

if __name__ == "__main__":
    main()