students = {}

while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[roll] = {"name": name, "marks": marks}
        print("Student added successfully.")

    elif choice == 2:
        roll = input("Enter roll number to search: ")
        if roll in students:
            print("Name:", students[roll]["name"])
            print("Marks:", students[roll]["marks"])
        else:
            print("Student not found.")

    elif choice == 3:
        roll = input("Enter roll number to update: ")
        if roll in students:
            name = input("Enter new name: ")
            marks = int(input("Enter new marks: "))
            students[roll] = {"name": name, "marks": marks}
            print("Student updated successfully.")
        else:
            print("Student not found.")

    elif choice == 4:
        roll = input("Enter roll number to delete: ")
        if roll in students:
            del students[roll]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == 5:
        if len(students) == 0:
            print("No students in database.")
        else:
            for roll, info in students.items():
                print("Roll:", roll, "| Name:", info["name"], "| Marks:", info["marks"])

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
