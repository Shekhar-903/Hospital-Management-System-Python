from database import connect_db
from utils import *

def add_patient():
    name = get_non_empty_string("Name: ")
    age = get_valid_age()
    gender = get_non_empty_string("Gender: ")
    disease = get_non_empty_string("Disease: ")
    phone = get_valid_phone()

    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO patient (name, age, gender, disease, phone) VALUES (?, ?, ?, ?, ?)",
        (name, age, gender, disease, phone)
    )
    conn.commit()
    conn.close()
    print("✅ Patient added successfully")

def view_patients():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patient")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("⚠️ No patients found.")
        return

    for row in rows:
        print(row)

def delete_patient():
    pid = get_valid_int("Enter Patient ID: ")

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patient WHERE patient_id=?", (pid,))
    if not cur.fetchone():
        print("❌ Patient ID not found.")
        conn.close()
        return

    cur.execute("DELETE FROM patient WHERE patient_id=?", (pid,))
    conn.commit()
    conn.close()
    print("🗑️ Patient deleted.")
