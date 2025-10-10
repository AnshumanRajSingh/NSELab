# --------------------------
# Caesar Cipher
# --------------------------
def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():  # Encrypt only letters
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(cipher, key):
    return caesar_encrypt(cipher, -key)


# --------------------------
# Vigenère Cipher
# --------------------------
def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(cipher, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in cipher:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result


# --------------------------
# Main Program
# --------------------------
if __name__ == "__main__":
    print("===== Classical Symmetric Ciphers =====")
    print("1. Caesar Cipher")
    print("2. Vigenere Cipher")
    choice = input("Choose a cipher (1/2): ")

    text = input("Enter the text to encrypt: ")

    if choice == "1":
        key = int(input("Enter Caesar key (number): "))
        encrypted = caesar_encrypt(text, key)
        decrypted = caesar_decrypt(encrypted, key)
        print("\n--- Caesar Cipher ---")
        print("Plaintext :", text)
        print("Encrypted :", encrypted)
        print("Decrypted :", decrypted)

    elif choice == "2":
        key = input("Enter Vigenere key (word): ")
        encrypted = vigenere_encrypt(text, key)
        decrypted = vigenere_decrypt(encrypted, key)
        print("\n--- Vigenere Cipher ---")
        print("Plaintext :", text)
        print("Encrypted :", encrypted)
        print("Decrypted :", decrypted)

    else:
        print("❌ Invalid choice!")
