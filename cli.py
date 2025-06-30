import argparse
from encryptor import generate_key, encrypt_file, decrypt_file

def main():
    parser = argparse.ArgumentParser(description="File Encryptor with Fernet")
    parser.add_argument("mode", choices=["encrypt", "decrypt", "genkey"], help="Operation mode")
    parser.add_argument("--key", help="Key file path (required for encrypt and decrypt)")
    parser.add_argument("--input", help="Input file path")
    parser.add_argument("--output", help="Output file path")

    args = parser.parse_args()

    if args.mode == "genkey":
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        print("Key generated and saved to secret.key")
        return

    if not args.key or not args.input or not args.output:
        print("For encrypt/decrypt you must specify --key, --input and --output")
        return

    with open(args.key, "rb") as key_file:
        key = key_file.read()

    if args.mode == "encrypt":
        encrypt_file(key, args.input, args.output)
        print(f"File encrypted: {args.output}")
    elif args.mode == "decrypt":
        decrypt_file(key, args.input, args.output)
        print(f"File decrypted: {args.output}")

if __name__ == "__main__":
    main()

