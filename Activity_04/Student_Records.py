students = []  
fileName = ''

# Menu
while True:
    print("=" * 60)
    print(" STUDENT RECORD MANAGEMENT SYSTEM ".center(60))
    print("=" * 60)
    print("[1] Open File")
    print("[2] Save File")
    print("[3] Save As File")
    print("[4] Show All Students")
    print("[5] Show Student Record")
    print("[6] Add Student")
    print("[7] Edit Student")
    print("[8] Delete Student")
    print("[0] Exit")
    print("-" * 60)
    
    choice = input("Enter your choice: ")

    # Open File
    if choice == '1':
        fileName = input('Enter file name to open: ')
        try:
            with open(fileName, 'r') as file:
                lines = file.readlines()
                students.clear()
                for i in range(0, len(lines), 4):
                    studentId = lines[i].strip().split(": ")[1]
                    fullName = lines[i+1].strip().split(": ")[1].split(" ")
                    classStanding = float(lines[i+2].strip().split(": ")[1])
                    majorExam = float(lines[i+3].strip().split(": ")[1])
                    students.append([studentId, (fullName[0], fullName[-1]), classStanding, majorExam])
            print("\nFile opened successfully.\n")
        except FileNotFoundError:
            print("\nError: File not found.\n")

    # Save File
    elif choice == '2':
        if fileName:
            with open(fileName, 'w') as file:
                for student in students:
                    file.write(f"Student ID: {student[0]}\n")
                    file.write(f"Student Name: {student[1][0]} {student[1][1]}\n")
                    file.write(f"Class Standing: {student[2]}\n")
                    file.write(f"Major Exam Grade: {student[3]}\n")
            print(f"\nRecords saved to {fileName}.\n")
        else:
            print("\nNo file opened. Use 'Save As' to specify a file.\n")

    # Save As File
    elif choice == '3':
        fileName = input('Enter file name: ')
        with open(fileName, 'w') as file:
            for student in students:
                file.write(f"Student ID: {student[0]}\n")
                file.write(f"Student Name: {student[1][0]} {student[1][1]}\n")
                file.write(f"Class Standing: {student[2]}\n")
                file.write(f"Major Exam Grade: {student[3]}\n")
        print(f"\nFile saved as {fileName}.\n")

    # Show All Students
    # Show All Students Record
    elif choice == '4':
        if not students:
            print("-" * 40)
            print("No student records available.")
            print("-" * 40)
            continue

        print("=" * 40)
        print("Show All Students Record Options:")
        print("=" * 40)
        print("[1] Order by Last Name")
        print("[2] Order by Grade")
        print("-" * 40)
        
        showRecordChoice = input("Enter your choice: ")

        # Order by last name
        if showRecordChoice == '1':
            for i in range(len(students) - 1):
                for j in range(i + 1, len(students)):
                    if students[i][1][1] > students[j][1][1]:
                        students[i], students[j] = students[j], students[i]

        # Order by computed grade
        elif showRecordChoice == '2':
            for i in range(len(students) - 1):
                for j in range(i + 1, len(students)):
                    gradeI = students[i][2] * 0.6 + students[i][3] * 0.4
                    gradeJ = students[j][2] * 0.6 + students[j][3] * 0.4
                    if gradeI < gradeJ:  # Descending order
                        students[i], students[j] = students[j], students[i]

        else:
            print("-" * 40)
            print("Invalid Choice.")
            print("-" * 40)
            continue

        print("=" * 80)
        print(f"{'ID':<10} {'Last Name':<15} {'First Name':<15} {'Class Standing':<15} {'Exam Grade':<10}")
        print("=" * 80)
        
        for student in students:
            print(f"{student[0]:<10} {student[1][1]:<15} {student[1][0]:<15} {student[2]:<15} {student[3]:<10}")
        
        print("=" * 80)


    # Show Student Record 
    elif choice == '5':
        searchId = input("Enter Student ID to view record: ")
        print("-" * 50)
        for student in students:
            if student[0] == searchId:
                print("\nStudent Record:")
                print("=" * 50)
                print(f"Student ID      : {student[0]}")
                print(f"Full Name       : {student[1][0]} {student[1][1]}")
                print(f"Class Standing  : {student[2]}")
                print(f"Major Exam Grade: {student[3]}")
                print("=" * 50)
                break
        else:
            print("\nStudent not found.\n")


    # Add Student
    elif choice == '6':
        studentId = input("Enter Student ID (6 digits): ")
        firstName = input("Enter First Name: ")
        lastName = input("Enter Last Name: ")
        classStanding = float(input("Enter Class Standing: "))
        majorExam = float(input("Enter Exam Grade: "))
        students.append([studentId, (firstName, lastName), classStanding, majorExam])
        print("\nStudent added successfully.\n")

    # Edit Student
    elif choice == '7':
        studentId = input("Enter Student ID to edit: ")
        
        for i in range(len(students)):
            if students[i][0] == studentId:
                newId = input("Enter new Student ID (Press Enter to skip): ") or students[i][0]
                newFirstName = input("Enter new First Name (Press Enter to skip): ") or students[i][1][0]
                newLastName = input("Enter new Last Name (Press Enter to skip): ") or students[i][1][1]
                newClassStanding = input("Enter new Class Standing (Press Enter to skip): ") or students[i][2]
                newMajorExam = input("Enter new Exam Grade (Press Enter to skip): ") or students[i][3]

                students[i] = [newId, (newFirstName, newLastName), float(newClassStanding), float(newMajorExam)]
                print("\nStudent record updated successfully.\n")
                break
        else:
            print("\nStudent not found.\n")

    # Delete Student
    elif choice == '8':
        studentId = input("Enter Student ID to delete: ")
        for i in range(len(students)):
            if students[i][0] == studentId:
                del students[i]
                print("\nStudent record deleted.\n")
                break
        else:
            print("\nStudent not found.\n")

    # Exit
    elif choice == '0':
        print("\nExiting program. Goodbye!\n")
        break

    else:
        print("\nInvalid choice. Try again.\n")
