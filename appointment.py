from database import connect_db
from utils import *

def book_appointment():
    conn = connect_db()
    cur = conn.cursor()

    pid = get_valid_int("Patient ID: ")
    cur.execute("SELECT * FROM patient WHERE patient_id=?", (pid,))
    if not cur.fetchone():
        print("❌ Patient not found.")
        conn.close()
        return

    did = get_valid_int("Doctor ID: ")
    cur.execute("SELECT * FROM doctor WHERE doctor_id=?", (did,))
    if not cur.fetchone():
        print("❌ Doctor not found.")
        conn.close()
        return

    date = get_valid_date()
    cur.execute(
        "INSERT INTO appointment (patient_id, doctor_id, date) VALUES (?, ?, ?)",
        (pid, did, date)
    )
    conn.commit()
    conn.close()
    print("📅 Appointment booked.")

def view_appointments():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
    SELECT a.appointment_id, p.name, d.name, a.date
    FROM appointment a
    JOIN patient p ON a.patient_id = p.patient_id
    JOIN doctor d ON a.doctor_id = d.doctor_id
    """)
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("⚠️ No appointments found.")
        return

    for row in rows:
        print(row)
