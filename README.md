# XOR-decrypting
This Python script decrypts files that have been encrypted using a simple XOR encryption algorithm. It prompts the user to provide the directory path containing encrypted files and the decryption key. Then, it proceeds to decrypt all files with the `.crypt` extension found in the specified directory.

## Usage

1. Clone the repository or download the script.
2. Ensure you have Python installed on your system.
3. Run the script using a Python interpreter.
4. Follow the on-screen prompts to enter the directory path and decryption key.
5. The script will decrypt all `.crypt` files in the specified directory and remove the encrypted files after decryption.

## Requirements

- Python 3.x

## How It Works

The script performs the following steps:

1. Prompts the user to input the directory path and decryption key.
2. Iterates through each file in the specified directory.
3. Identifies files with the `.crypt` extension.
4. Decrypts each encrypted file using XOR encryption with the provided decryption key.
5. Writes the decrypted content to a new file.
6. Removes the original encrypted file.

## Note

- Ensure you have permission to read from and write to the specified directory.
- Use caution when specifying the decryption key to ensure correct decryption of files.

## Example

```bash
$ python main.py
Enter the directory path: /path/to/encrypted/files
Enter the decryption key: my_secret_key
Decryption successful.
Exiting...
