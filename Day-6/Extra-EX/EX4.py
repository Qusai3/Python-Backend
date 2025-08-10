def main():
    counts = {200: 0, 404: 0, 500: 0}
    malformed = 0

    try:
        with open("server.log", "r", encoding="utf-8") as fin:
            for line in fin:
                text = line.strip()
                if not text:
                    continue
                parts = text.split(maxsplit=2)  
                if len(parts) < 3:
                    malformed += 1
                    continue
                ip, status_str, url = parts[0], parts[1], parts[2]
                try:
                    status = int(status_str)
                except ValueError:
                    malformed += 1
                    continue

                if status in counts:
                    counts[status] += 1
                

        with open("report.txt", "w", encoding="utf-8") as fout:
            fout.write(f"Successful (200): {counts[200]}\n")
            fout.write(f"Not Found (404): {counts[404]}\n")
            fout.write(f"Server Error (500): {counts[500]}\n")

        print("Report written to 'report.txt'. "
              f"Malformed/ignored lines: {malformed}")

    except FileNotFoundError:
        print("Error: 'server.log' not found.")
    except PermissionError:
        print("Error: permission denied reading or writing files.")
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    main()