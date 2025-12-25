from database import create_tables
from patient import *
from doctor import *
from appointment import *

create_tables()

while True:
    print("""
🏥 Hospital Management System
1. Add Patient
2. View Patients
3. Delete Patient
4. Add Doctor
5. View Doctors
6. Book Appointment
7. View Appointments
8. Exit
""")

    choice = input("Choose option: ")

    if choice == "1": add_patient()
    elif choice == "2": view_patients()
    elif choice == "3": delete_patient()
    elif choice == "4": add_doctor()
    elif choice == "5": view_doctors()
    elif choice == "6": book_appointment()
    elif choice == "7": view_appointments()
    elif choice == "8":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")
