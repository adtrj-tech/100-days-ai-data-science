students = []


def calculate_average(marks):
    return sum(marks) / len(marks)


def find_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter student name: ")

    try:
        mark1 = float(input("Enter mark for Subject 1: "))
        mark2 = float(input("Enter mark for Subject 2: "))
        mark3 = float(input("Enter mark for Subject 3: "))

        marks = [mark1, mark2, mark3]

        for mark in marks:
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return

        average = calculate_average(marks)
        grade = find_grade(average)

        student = {
            "name": name,
            "marks": marks,
            "average": average,
            "grade": grade
        }

        students.append(student)

        print("Student added successfully!")

    except ValueError:
        print("Please enter valid numeric marks.")


def display_students():
    if not students:
        print("No student records available.")
        return

    print("\n----- Student Records -----")

    for student in students:
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Average:", round(student["average"], 2))
        print("Grade:", student["grade"])
        print("---------------------------")


def find_top_student():
    if not students:
        print("No student records available.")
        return

    top_student = max(students, key=lambda student: student["average"])

    print("\n----- Top Student -----")
    print("Name:", top_student["name"])
    print("Average:", round(top_student["average"], 2))
    print("Grade:", top_student["grade"])


def save_report():
    if not students:
        print("No student records to save.")
        return

    with open("student_report.txt", "w") as file:
        for student in students:
            file.write(f"Name: {student['name']}\n")
            file.write(f"Marks: {student['marks']}\n")
            file.write(f"Average: {round(student['average'], 2)}\n")
            file.write(f"Grade: {student['grade']}\n")
            file.write("---------------------------\n")

    print("Report saved successfully!")


def main():
    while True:
        print("\n===== Student Performance System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Find Top Student")
        print("4. Save Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            find_top_student()

        elif choice == "4":
            save_report()

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Try again.")


main()