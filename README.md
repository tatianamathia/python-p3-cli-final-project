# Phase 3 CLI project 

# PROJECT NAME-Student Medical Record 
This is a CLI-based application to manage student medical records. It allows users to manage students, their medical visits, and associated medical issues. The application uses a database to store and retrieve data.

# CLI Script Overview
Purpose
The CLI script provides a command-line interface for managing students, visits, and medical issues in a healthcare or educational context. It allows users to perform CRUD operations (Create, Read, Update, Delete) on these entities stored in a database.

# Features
Manage Students: Add, delete, view all, and find students by ID.
Manage Visits: Add, delete, view all, and find visits by ID.
Manage Medical Issues: Add, delete, view all, and find medical issues by ID.
Interaction with Database
The CLI interacts with a SQLite database to store and retrieve information about students, visits, and medical issues. Each entity (student, visit, medical issue) corresponds to a table in the database, and CRUD operations are performed using SQL queries.

# Error Handling
The CLI includes basic error handling to manage input validation and database operations. Error messages are provided to guide users when input is invalid or when operations fail.

# Customization and Extensibility
Users can extend the CLI by adding new commands or modifying existing functionalities. The modular structure allows for easy customization to fit specific project requirements.

# Security Considerations
Ensure the database connection details are handled securely, and sensitive data (if any) is managed following best practices for data protection.

# Limitations
Currently supports SQLite database only.
Limited error handling beyond basic input validation.
Future Enhancements
Implement user authentication and authorization for secure access.
Support for multiple database backends (e.g., PostgreSQL, MySQL).
Enhanced error handling and logging capabilities.
# Functionality
cli.py
The main CLI script (cli.py) serves as the entry point for interacting with the application. It includes the following functionalities:

Main Menu: Provides options to manage students, visits, medical issues, and exit the program.
Manage Students: Submenu to add, delete, view all, and find students by ID.
Manage Visits: Submenu to add, delete, view all, and find visits by ID.
Manage Medical Issues: Submenu to add, delete, view all, and find medical issues by ID.
models.py
Defines classes for each entity (Student, Visit, MedicalIssue) with methods to interact with the database. Includes CRUD operations such as creating, deleting, retrieving all, and finding by ID.

db.py
Contains the database configuration (get_db) and connection management functions. Uses SQLite for data storage and retrieval operations.

# Installation
Clone the repository and install dependencies:

bash
Copy code
git clone https://github.com/tatianamathia/python-p3-cli-final-project
cd your-repo
pip install -r requirements.txt

# Usage
Navigate to the project directory and run the CLI script:

bash
Copy code
python cli.py
Follow the prompts to manage students, visits, and medical issues as described in the CLI Script Overview section.

# Models
Student
Attributes: id, name, gender
Methods:
create(name, gender): Adds a new student to the database.
delete(student_id): Deletes a student from the database.
get_all(): Retrieves all students from the database.
find_by_id(student_id): Finds a student by their ID.
Visit
Attributes: id, student_id, medical_issue_id, date
Methods:
create(student_id, medical_issue_id, date): Adds a new visit to the database.
delete(visit_id): Deletes a visit from the database.
get_all(): Retrieves all visits from the database.
find_by_id(visit_id): Finds a visit by its ID.
MedicalIssue
Attributes: id, description, severity, treatment
Methods:
create(description, severity, treatment): Adds a new medical issue to the database.
delete(medical_issue_id): Deletes a medical issue from the database.
get_all(): Retrieves all medical issues from the database.
find_by_id(medical_issue_id): Finds a medical issue by its ID.

# Contributing
[Provide guidelines for how others can contribute to your project, including reporting issues, submitting pull requests, etc.]

# License
© 2024 Student Medical Record. This project is licensed under the MIT License.