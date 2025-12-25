from database import create_tables
from patient import add_patient, view_patients, delete_patient
from doctor import add_doctor, view_doctors
from appointment import book_appointment, view_appointments

def menu():
    print("\n🏥 Hospital Management System")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Delete Patient")
    print("4. Add Doctor")
    print("5. View Doctors")
    print("6. Book Appointment")
    print("7. View Appointments")
    print("8. Exit")

create_tables()

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_patients()
    elif choice == "3":
        delete_patient()
    elif choice == "4":
        add_doctor()
    elif choice == "5":
        view_doctors()
    elif choice == "6":
        book_appointment()
    elif choice == "7":
        view_appointments()
    elif choice == "8":
        print("👋 Exiting system")
        break
    else:
        print("❌ Invalid choice")
