from database import connect_db
from utils import *

def add_doctor():
    name = get_non_empty_string("Doctor Name: ")
    specialization = get_non_empty_string("Specialization: ")

    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO doctor (name, specialization) VALUES (?, ?)",
        (name, specialization)
    )
    conn.commit()
    conn.close()
    print("✅ Doctor added.")

def view_doctors():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM doctor")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("⚠️ No doctors available.")
        return

    for row in rows:
        print(row)
