# Client connecting to server
import socket
import json
from datetime import datetime

PORT = 5050
SERVER = "127.0.0.1"

VALID_MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

COURSES = {
    "1": "MSc Cyber Security",
    "2": "MSc Information Systems & Computing",
    "3": "MSc Data Analytics"
}



def validate_name(name):
    return name.replace(" ", "").isalpha()


def validate_year(start_year):
    return start_year.isdigit() and len(start_year) == 4 and int(start_year) >= datetime.now().year


def validate_month(start_month):
    return start_month.capitalize() in VALID_MONTHS


def validate_course(choice):
    return choice in COURSES


def validate_details(student_details):
    errors = {}

    if not validate_name(student_details["name"]):
        errors["name"] = "Name cannot be empty and must contain no numbers."

    if not student_details["address"].strip():
        errors["address"] = "Address cannot be empty."

    if not student_details["education"].strip():
        errors["education"] = "Education field cannot be empty."

    if not validate_year(student_details["start_year"]):
        errors["start_year"] = "Year must be a 4-digit number >= current year."

    if not validate_month(student_details["start_month"]):
        errors["start_month"] = "Month must be a valid month name (e.g., January)."

    return errors


# GET USER INPUT

def get_student_details():
    student_details = {}

    print(" DBS Student Application Form \n")
    print("-----------------------------  \n")
    student_details["name"] = input(f"Enter your full name: ")
    student_details["address"] = input(f"Enter your address: ")
    student_details["education"] = input(f"Enter your education qualifications: ")

    print("\nSelect Course:")
    for key, value in COURSES.items():
        print(f"{key}. {value}")

    course_choice = input("Enter option (1/2/3): ").strip()
    student_details["course"] = COURSES.get(course_choice, "MSc Cyber Security")
    student_details["start_year"] = input("Enter intended start Year (e.g. 2026): ")
    student_details["start_month"] = input("Enter intended start Month (e.g. April): ")

    return student_details


# Confirming details and submitting

def confirm_details(student_details):
    while True:
        print("\n PLEASE CONFIRM YOUR DETAILS")
        print("--------------------------------")
        for key, value in student_details.items():
            print(f"{key.capitalize()}: {value}")

        errors = validate_details(student_details)

        if errors:
            print("Some fields are invalid:")
            for field, msg in errors.items():
                print(f"- {field}: {msg}")

        print("\nOptions:")
        print("1. Edit  again")
        print("2. Save and submit")

        choice = input("Enter option (1/2): ").strip()

        if choice == "1":
            student_details = get_student_details()
        elif choice == "2":
            if not errors:
                return student_details
            else:
                print("\n Cannot save. Fix the errors first.")
        else:
            print("Invalid choice, try again.")

# Client socket

def start_client():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER, PORT))
        print("\nConnected to server.\n")

        #  Using get_student_details function and confirm_details 
        details = get_student_details()
        final_details = confirm_details(details)
       # Send JSON to server
        client.send(json.dumps(final_details).encode())

        #  Receive response (unique number)
        response = client.recv(1024).decode()
        print(f"Your application reference is ", response)

        client.close()

    except Exception as e:
        print("Error submitting details")


if __name__ == "__main__":
    start_client()
