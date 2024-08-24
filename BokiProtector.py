import hashlib
import secrets  # More secure than random for cryptographic purposes


def hash_password(password: str) -> str:
    # Generate a more secure salt
    salt = f"Boki-Protector-{secrets.randbelow(1999 - 122) + 122}-"

    # Combine salt and password
    salted_password = salt + password

    # Hash the salted password
    hashed = hashlib.sha3_512(salted_password.encode()).hexdigest()

    return hashed


if __name__ == "__main__":
    # Prompt the user for their password
    password = input("[INFO] Enter your password: ")

    # Hash the password
    hashed_password = hash_password(password)

    # Show the result
    print("[SUCCESS] Here is the hashed password:")
    print(hashed_password)

    # Pause the console before closing
    input("[INFO] Press Enter to close the program")
