import tkinter as tk
from tkinter import messagebox
import csv

def add_student():
    student_id = student_id_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    
    try:
        age = int(age_entry.get())
        grade = float(grade_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Age should be an integer, and Grade should be a number.")
        return

    student = {
        "Student ID": student_id,
        "First Name": first_name,
        "Last Name": last_name,
        "Age": age,
        "Grade": grade
    }
    
    students.append(student)
    messagebox.showinfo("Success", "Student added successfully!")
    clear_entries()

def view_students():
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    
    for student in students:
        result_text.insert(tk.END, f"Student ID: {student['Student ID']}\n")
        result_text.insert(tk.END, f"First Name: {student['First Name']}\n")
        result_text.insert(tk.END, f"Last Name: {student['Last Name']}\n")
        result_text.insert(tk.END, f"Age: {student['Age']}\n")
        result_text.insert(tk.END, f"Grade: {student['Grade']}\n")
        result_text.insert(tk.END, "----------------\n")
    
    result_text.config(state=tk.DISABLED)

def search_student():
    name_to_search = search_name_entry.get()
    found_students = []

    for student in students:
        if name_to_search.lower() in (student["First Name"].lower() + " " + student["Last Name"].lower()):
            found_students.append(student)

    if found_students:
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        
        for student in found_students:
            result_text.insert(tk.END, f"Student ID: {student['Student ID']}\n")
            result_text.insert(tk.END, f"First Name: {student['First Name']}\n")
            result_text.insert(tk.END, f"Last Name: {student['Last Name']}\n")
            result_text.insert(tk.END, f"Age: {student['Age']}\n")
            result_text.insert(tk.END, f"Grade: {student['Grade']}\n")
            result_text.insert(tk.END, "----------------\n")
        
        result_text.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("Search Result", "Student not found.")

def remove_student():
    student_id_to_remove = remove_id_entry.get()
    for student in students:
        if student["Student ID"] == student_id_to_remove:
            students.remove(student)
            messagebox.showinfo("Success", "Student removed successfully!")
            clear_entries()
            return
    messagebox.showinfo("Remove Student", "Student not found.")

def clear_entries():
    student_id_entry.delete(0, tk.END)
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    search_name_entry.delete(0, tk.END)
    remove_id_entry.delete(0, tk.END)

def exit_program():
    with open("student_records.csv", mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Student ID", "First Name", "Last Name", "Age", "Grade"])
        writer.writeheader()
        writer.writerows(students)
    
    window.destroy()

# Initialize the tkinter window
window = tk.Tk()
window.title("Student Management System")

# Create a list to store student records
students = []

# Labels
student_id_label = tk.Label(window, text="Student ID:")
first_name_label = tk.Label(window, text="First Name:")
last_name_label = tk.Label(window, text="Last Name:")
age_label = tk.Label(window, text="Age:")
grade_label = tk.Label(window, text="Grade:")
search_name_label = tk.Label(window, text="Search by Name:")
remove_id_label = tk.Label(window, text="Student ID to Remove:")

# Entry widgets
student_id_entry = tk.Entry(window)
first_name_entry = tk.Entry(window)
last_name_entry = tk.Entry(window)
age_entry = tk.Entry(window)
grade_entry = tk.Entry(window)
search_name_entry = tk.Entry(window)
remove_id_entry = tk.Entry(window)

# Buttons
add_button = tk.Button(window, text="Add Student", command=add_student)
view_button = tk.Button(window, text="View Students", command=view_students)
search_button = tk.Button(window, text="Search Student", command=search_student)
remove_button = tk.Button(window, text="Remove Student", command=remove_student)
exit_button = tk.Button(window, text="Exit", command=exit_program)

# Text widget to display student records
result_text = tk.Text(window, height=15, width=40)
result_text.config(state=tk.DISABLED)

# Place widgets on the window
student_id_label.grid(row=0, column=0)
first_name_label.grid(row=1, column=0)
last_name_label.grid(row=2, column=0)
age_label.grid(row=3, column=0)
grade_label.grid(row=4, column=0)
search_name_label.grid(row=6, column=0)
remove_id_label.grid(row=8, column=0)

student_id_entry.grid(row=0, column=1)
first_name_entry.grid(row=1, column=1)
last_name_entry.grid(row=2, column=1)
age_entry.grid(row=3, column=1)
grade_entry.grid(row=4, column=1)
search_name_entry.grid(row=6, column=1)
remove_id_entry.grid(row=8, column=1)

add_button.grid(row=5, column=0, columnspan=2)
view_button.grid(row=7, column=0, columnspan=2)
search_button.grid(row=9, column=0, columnspan=2)
remove_button.grid(row=10, column=0, columnspan=2)
exit_button.grid(row=11, column=0, columnspan=2)

result_text.grid(row=0, column=2, rowspan=12, padx=10, pady=10)

# Start the tkinter main loop
window.mainloop()
