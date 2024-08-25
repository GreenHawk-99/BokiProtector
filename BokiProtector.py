import hashlib
import secrets  # More secure than random for cryptographic purposes


def hash_password(given_password: str, given_salt: str) -> str:

    if given_salt:
        try:
            # Generate a less secure salt
            salt = f"Boki-Protector-{int(given_salt)}-"
        except ValueError:
            # Generate a more secure salt
            print("[ERROR] Invalid salt. Using a random secure salt instead.")
            salt = f"Boki-Protector-{secrets.randbelow(1999 - 122) + 122}-"
    else:
        print("[INFO] Custom salt skipped")
        # Generate a more secure salt
        salt = f"Boki-Protector-{secrets.randbelow(1999 - 122) + 122}-"

    # Combine salt and password
    salted_password = salt + given_password

    # Hash the salted password
    hashed = hashlib.sha3_512(salted_password.encode()).hexdigest()

    return hashed


if __name__ == "__main__":
    # Prompt the user for their password
    password = input("[INFO] Enter your password: ")
    custom_salt = input("[INFO] (Optional) Enter your custom salt (must be a number) "
                        "or press 'Enter' to skip: ")

    # Hash the password
    hashed_password = hash_password(password, custom_salt)

    # Show the result
    print("[SUCCESS] Here is the hashed password:")
    print(hashed_password)

    # Pause the console before closing
    input("[INFO] Press 'Enter' to close the program")
