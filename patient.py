from database import connect_db

def add_patient():
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    disease = input("Disease: ")
    phone = input("Phone: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO patient (name, age, gender, disease, phone) VALUES (?, ?, ?, ?, ?)",
        (name, age, gender, disease, phone)
    )
    conn.commit()
    conn.close()
    print("✅ Patient added successfully")

def view_patients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patient")
    rows = cursor.fetchall()
    conn.close()

    print("\n--- Patient List ---")
    for row in rows:
        print(row)

def delete_patient():
    pid = int(input("Enter Patient ID to delete: "))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patient WHERE patient_id = ?", (pid,))
    conn.commit()
    conn.close()
    print("🗑️ Patient deleted successfully")
