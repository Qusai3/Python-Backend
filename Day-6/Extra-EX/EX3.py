class InvalidLengthError(Exception):
    """Username length is < 5 or > 15 characters."""

class InvalidCharacterError(Exception):
    """Username contains non-alphanumeric characters."""

def validate_username(name: str):
    if len(name) < 5 or len(name) > 15:
        raise InvalidLengthError("Username must be 5–15 characters long.")
    if not name.isalnum():
        raise InvalidCharacterError("Username must contain only letters and numbers.")

def main():
    status_msg = "Registration not attempted."
    try:
        username = input("Enter a username (5–15 chars, letters and numbers only): ").strip()
        validate_username(username)

        # If we reach here, it's valid
        with open("users.txt", "a", encoding="utf-8") as f:
            f.write(username + "\n")

        print("Success: username registered!")
        status_msg = "Registration succeeded."
    except InvalidLengthError as e:
        print("Invalid length:", e)
        status_msg = "Registration failed (length rule)."
    except InvalidCharacterError as e:
        print("Invalid character(s):", e)
        status_msg = "Registration failed (character rule)."
    except PermissionError:
        print("Error: cannot write to 'users.txt' (permission denied).")
        status_msg = "Registration failed (file write error)."
    except Exception as e:
        print("Unexpected error:", e)
        status_msg = "Registration failed (unexpected error)."
    finally:
        print("Status:", status_msg)

if __name__ == "__main__":
    main()