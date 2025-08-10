from os import name


def clean(word: str) -> str:
    """Lowercase and remove simple punctuation around a word."""
    punctuation = ".,!?;:'()[]{}<>-—*_#/$\\\""
    return word.strip(punctuation).lower()

def main():
    filename = input("Enter the path to the text file: ").strip()

    counts = {}  

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                words = line.split()          # split by whitespace
                for w in words:
                    w = clean(w)
                    if not w:                  # skip empty strings
                        continue
                    counts[w] = counts.get(w, 0) + 1

    except FileNotFoundError:
        print("Error: file not found. Check the name/path and try again.")
        return
    except PermissionError:
        print("Error: you don't have permission to read this file.")
        return
    except IsADirectoryError:
        print("Error: that path is a directory, not a file.")
        return
    except UnicodeDecodeError:
        print("Error: could not read the file text (encoding issue).")
        return
    except Exception as e:
        print("Unexpected error:", e)
        return

    # Show results (sorted by highest frequency)
    print("\nWord frequencies:\n-----------------")
    for word, freq in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()