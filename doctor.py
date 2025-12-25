from database import connect_db

def add_doctor():
    name = input("Doctor Name: ")
    specialization = input("Specialization: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO doctor (name, specialization) VALUES (?, ?)",
        (name, specialization)
    )
    conn.commit()
    conn.close()
    print("✅ Doctor added successfully")

def view_doctors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctor")
    rows = cursor.fetchall()
    conn.close()

    print("\n--- Doctor List ---")
    for row in rows:
        print(row)
