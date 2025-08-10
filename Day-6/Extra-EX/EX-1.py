def is_palindrome(word: str) -> bool:
    """Check if a word is a palindrome (case-insensitive)."""
    word = word.lower()
    return word == word[::-1]

def main():
    input_file = "input_words.txt"
    output_file = "palindromes.txt"

    try:
        # Read words from file
        with open(input_file, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]  # remove empty lines

        # Find palindromes
        palindromes = [word.upper() for word in words if is_palindrome(word)]

        # Write palindromes to new file
        with open(output_file, "w", encoding="utf-8") as f:
            for p in palindromes:
                f.write(p + "\n")

        print(f"Done! Found {len(palindromes)} palindrome(s). See '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")
    except PermissionError:
        print("Error: You don't have permission to read/write the file.")
    except UnicodeDecodeError:
        print("Error: Could not read the file text (encoding issue).")
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    main()
