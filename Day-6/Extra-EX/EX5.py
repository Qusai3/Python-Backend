SPECIALS = "!@#$%^&*"

def check_password(pw: str):
    """Return (is_valid, error_messages_list)."""
    errors = []
    if len(pw) < 8:
        errors.append("Must be at least 8 characters.")
    if not any(c.islower() for c in pw):
        errors.append("Must contain a lowercase letter.")
    if not any(c.isupper() for c in pw):
        errors.append("Must contain an uppercase letter.")
    if not any(c.isdigit() for c in pw):
        errors.append("Must contain a digit.")
    if not any(c in SPECIALS for c in pw):
        errors.append(f"Must contain a special character ({SPECIALS}).")
    return (len(errors) == 0, errors)

def main():
    in_file = "passwords.txt"
    out_file = "strong_passwords.txt"
    err_file = "password_validation_errors.txt"

    strong = 0
    weak = 0

    try:
        with open(in_file, "r", encoding="utf-8") as fin, \
             open(out_file, "w", encoding="utf-8") as fout, \
             open(err_file, "w", encoding="utf-8") as ferr:

            for line in fin:
                pw = line.rstrip("\n")
                if not pw:
                    continue
                ok, errs = check_password(pw)
                if ok:
                    fout.write(pw + "\n")
                    strong += 1
                else:
                    weak += 1
                    ferr.write(f"{pw} -> " + "; ".join(errs) + "\n")

        print(f"Done! Strong: {strong}, Weak: {weak}.")
        print(f"See '{out_file}' and '{err_file}' for details.")

    except FileNotFoundError:
        print(f"Error: '{in_file}' not found.")
    except PermissionError:
        print("Error: permission denied reading or writing files.")
    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()