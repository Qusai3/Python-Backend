import json
import os

DATA_FILE = "students.json"

def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=2)

# ---------- basic actions ----------
def add_student(students):
    sid = input("Enter ID: ").strip()
    name = input("Enter name: ").strip()
    age_text = input("Enter age: ").strip()

    if not sid or not name or not age_text.isdigit():
        print("Invalid input. Try again.")
        return

    # check duplicate ID
    for s in students:
        if s["id"] == sid:
            print("ID already exists.")
            return
    students.append({"id": sid, "name": name, "age": int(age_text)})
    save_students(students)
    print("Student added.")

def list_students(students):
    if not students:
        print("No students yet.")
        return
    # print simple table (no external libs)
    print("\nID\tName\tAge")
    print("--\t----\t---")
    for s in students:
        print(f'{s["id"]}\t{s["name"]}\t{s["age"]}')
    print()

def find_student(students):
    sid = input("Enter ID to find: ").strip()
    for s in students:
        if s["id"] == sid:
            print("Found:", s)
            return
    print("Not found.")

def delete_student(students):
    sid = input("Enter ID to delete: ").strip()
    for i, s in enumerate(students):
        if s["id"] == sid:
            students.pop(i)
            save_students(students)
            print("Deleted.")
            return
    print("Not found.")

def update_student(students):
    sid = input("Enter ID to update: ").strip()
    for s in students:
        if s["id"] == sid:
            new_name = input(f'New name (Enter to keep "{s["name"]}"): ').strip()
            new_age  = input(f'New age  (Enter to keep {s["age"]}): ').strip()

            if new_name:
                s["name"] = new_name
            if new_age:
                if new_age.isdigit():
                    s["age"] = int(new_age)
                else:
                    print("Age must be a number. Skipping age update.")

            save_students(students)
            print("Updated.")
            return
    print("Not found.")

def main():
    students = load_students()

    while True:
        print("\nStudent DB")
        print("1) Add student")
        print("2) List students")
        print("3) Find student by ID")
        print("4) Update student")
        print("5) Delete student")
        print("0) Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            find_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

    