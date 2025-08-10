def c_to_f(c):
    return (c * 9/5) + 32

def main():
    in_file = "celsius.txt"
    out_file = "fahrenheit.txt"
    bad_lines = 0
    total_lines = 0

    try:
        with open(in_file, "r", encoding="utf-8") as fin, \
             open(out_file, "w", encoding="utf-8") as fout:

            for line in fin:
                text = line.strip()
                if not text:
                    continue
                total_lines += 1
                try:
                    c = float(text)
                    f = c_to_f(c)
                    # formatted output
                    fout.write(f"{c:.2f}C = {f:.2f}F\n")
                except ValueError:
                    bad_lines += 1
                    # ignore this line and continue

        print(f"Done! Wrote results to '{out_file}'. "
              f"Processed {total_lines} number(s), skipped {bad_lines} bad line(s).")

    except FileNotFoundError:
        print(f"Error: '{in_file}' not found.")
    except PermissionError:
        print("Error: permission denied reading or writing the file(s).")
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    main()