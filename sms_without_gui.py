import csv

# Function to add a new student
def add_student(students):
    student_id = input("Enter Student ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    
    try:
        age = int(input("Enter Age: "))
        grade = float(input("Enter Grade: "))
    except ValueError:
        print("Invalid input. Age should be an integer, and Grade should be a number.")
        return

    student = {
        "Student ID": student_id,
        "First Name": first_name,
        "Last Name": last_name,
        "Age": age,
        "Grade": grade
    }
    
    students.append(student)
    print("Student added successfully!")

# Function to view all students
def view_students(students):
    print("Student Records:")
    for student in students:
        print("Student ID:", student["Student ID"])
        print("First Name:", student["First Name"])
        print("Last Name:", student["Last Name"])
        print("Age:", student["Age"])
        print("Grade:", student["Grade"])
        print("----------------")

# Function to search for a student by name
def search_student(students):
    name_to_search = input("Enter the name to search for: ")
    for student in students:
        if name_to_search.lower() in (student["First Name"].lower() + " " + student["Last Name"].lower()):
            print("Student found:")
            print("Student ID:", student["Student ID"])
            print("First Name:", student["First Name"])
            print("Last Name:", student["Last Name"])
            print("Age:", student["Age"])
            print("Grade:", student["Grade"])
            return
    print("Student not found.")

# Function to remove a student
def remove_student(students):
    student_id_to_remove = input("Enter the Student ID to remove: ")
    for student in students:
        if student["Student ID"] == student_id_to_remove:
            students.remove(student)
            print("Student removed successfully!")
            return
    print("Student not found.")

# Function to save data to a CSV file
def save_to_csv(students, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Student ID", "First Name", "Last Name", "Age", "Grade"])
        writer.writeheader()
        writer.writerows(students)

def main():
    students = []
    csv_filename = "student_records.csv"
    
    try:
        with open(csv_filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        pass

    while True:
        print("\nWelcome to the Student Management System!")
        print(" Menu:")
        print(" 1. Add a new student")
        print(" 2. View all students")
        print(" 3. Search for a student by name")
        print(" 4. Remove a student")
        print(" 5. Save and Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            remove_student(students)
        elif choice == "5":
            save_to_csv(students, csv_filename)
            print("Data saved to", csv_filename)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
