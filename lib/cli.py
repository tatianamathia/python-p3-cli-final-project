import sys
from db.students import Student
from db.visit import Visit
from db.medical_issue import MedicalIssue

def main_menu():
    while True:
        print("Main Menu")
        print("1. Manage Students")
        print("2. Manage Visits")
        print("3. Manage Medical Issues")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_students()
        elif choice == "2":
            manage_visits()
        elif choice == "3":
            manage_medical_issues()
        elif choice == "4":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def manage_students():
    while True:
        print("Manage Students")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. View All Students")
        print("4. Find Student by ID")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            gender = input("Enter student's gender: ")
            student_id = Student.create(name, gender)
            print(f"Student created with ID: {student_id}")
        elif choice == "2":
            student_id = input("Enter student ID to delete: ")
            Student.delete(student_id)
            print(f"Student with ID {student_id} deleted.")
        elif choice == "3":
            students = Student.get_all()
            for student in students:
                print(student)
        elif choice == "4":
            student_id = input("Enter student ID to find: ")
            student = Student.find_by_id(student_id)
            print(student)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_visits():
    while True:
        print("Manage Visits")
        print("1. Add Visit")
        print("2. Delete Visit")
        print("3. View All Visits")
        print("4. Find Visit by ID")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            medical_issue_id = input("Enter medical issue ID: ")
            date = input("Enter visit date: ")
            visit_id = Visit.create(student_id, medical_issue_id, date)
            print(f"Visit created with ID: {visit_id}")
        elif choice == "2":
            visit_id = input("Enter visit ID to delete: ")
            Visit.delete(visit_id)
            print(f"Visit with ID {visit_id} deleted.")
        elif choice == "3":
            visits = Visit.get_all()
            for visit in visits:
                print(visit)
        elif choice == "4":
            visit_id = input("Enter visit ID to find: ")
            visit = Visit.find_by_id(visit_id)
            print(visit)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_medical_issues():
    while True:
        print("Manage Medical Issues")
        print("1. Add Medical Issue")
        print("2. Delete Medical Issue")
        print("3. View All Medical Issues")
        print("4. Find Medical Issue by ID")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter medical issue description: ")
            severity = input("Enter severity: ")
            treatment = input("Enter treatment: ")
            medical_issue_id = MedicalIssue.create(description, severity, treatment)
            print(f"Medical issue created with ID: {medical_issue_id}")
        elif choice == "2":
            medical_issue_id = input("Enter medical issue ID to delete: ")
            MedicalIssue.delete(medical_issue_id)
            print(f"Medical issue with ID {medical_issue_id} deleted.")
        elif choice == "3":
            medical_issues = MedicalIssue.get_all()
            for issue in medical_issues:
                print(issue)
        elif choice == "4":
            medical_issue_id = input("Enter medical issue ID to find: ")
            issue = MedicalIssue.find_by_id(medical_issue_id)
            print(issue)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
