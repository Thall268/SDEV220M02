
""""
Author: Tyler Hall
Date Written: 3/16/2025
Assignment: Module 2 Lab - Case Study: if...else and while
Description: This Python program accepts student names and GPAs, checks if they qualify for the Dean's List or Honor Roll, and stores the results. It displays the qualifications and saves them to a file.
"""
class Student:
    def __init__(self, first_name, last_name, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
        self.dean_list = False
        self.honor_roll = False

    def check_qualification(self):
        """Check and assign qualification status based on GPA."""
        if self.gpa >= 3.5:
            self.dean_list = True
        elif self.gpa >= 3.25:
            self.honor_roll = True

    def __str__(self):
        """Return the student's qualification status as a string."""
        status = f"{self.first_name} {self.last_name} - GPA: {self.gpa}\n"
        if self.dean_list:
            status += "Made the Dean's List!\n"
        if self.honor_roll:
            status += "Made the Honor Roll!\n"
        return status


def get_student_data():
    """Prompt the user for student data and validate it."""
    while True:
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
        if last_name == 'ZZZ':
            print("Exiting student record processing.")
            break

        first_name = input("Enter student's first name: ")

        try:
            gpa = float(input("Enter student's GPA: "))
            if gpa < 0 or gpa > 4.0:
                print("GPA must be between 0.0 and 4.0. Please try again.")
                continue
        except ValueError:
            print("Invalid GPA input. Please enter a numeric value.")
            continue

        student = Student(first_name, last_name, gpa)
        student.check_qualification()
        students.append(student)

def display_students():
    """Display all student records."""
    if not students:
        print("No students have been entered.")
    else:
        for student in students:
            print(student)

def save_to_file(filename="students_results.txt"):
    """Save the results to a file."""
    with open(filename, "w") as file:
        if not students:
            file.write("No students have been entered.\n")
        else:
            for student in students:
                file.write(str(student) + "\n")
    print(f"Results saved to {filename}")

# Main program
students = []

# Get student data and process it
get_student_data()

# Display student qualifications
display_students()

# Save results to a file
save_to_file()

