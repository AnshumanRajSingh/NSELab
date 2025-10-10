import hashlib

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def verify_integrity(original, new_data):
    return generate_hash(original) == generate_hash(new_data)

# --------------------------
# Main Program
# --------------------------
if __name__ == "__main__":
    text = input("Enter the original text: ")
    hash_value = generate_hash(text)
    print("SHA-256 Hash:", hash_value)

    check_text = input("Enter text to verify: ")
    if verify_integrity(text, check_text):
        print("✅ Data is intact (No tampering detected).")
    else:
        print("❌ Data has been tampered with!")
