from database import connect_db

def book_appointment():
    patient_id = int(input("Patient ID: "))
    doctor_id = int(input("Doctor ID: "))
    date = input("Appointment Date (YYYY-MM-DD): ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO appointment (patient_id, doctor_id, date) VALUES (?, ?, ?)",
        (patient_id, doctor_id, date)
    )
    conn.commit()
    conn.close()
    print("📅 Appointment booked successfully")

def view_appointments():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT appointment.appointment_id, patient.name, doctor.name, appointment.date
    FROM appointment
    JOIN patient ON appointment.patient_id = patient.patient_id
    JOIN doctor ON appointment.doctor_id = doctor.doctor_id
    """)
    rows = cursor.fetchall()
    conn.close()

    print("\n--- Appointments ---")
    for row in rows:
        print(row)
