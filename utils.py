def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("❌ Input cannot be empty.")

def get_valid_age():
    while True:
        try:
            age = int(input("Age: "))
            if 0 < age < 120:
                return age
            print("❌ Enter valid age.")
        except ValueError:
            print("❌ Age must be a number.")

def get_valid_phone():
    while True:
        phone = input("Phone (10 digits): ")
        if phone.isdigit() and len(phone) == 10:
            return phone
        print("❌ Invalid phone number. Try again.")

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")

def get_valid_date():
    while True:
        date = input("Date (YYYY-MM-DD): ")
        parts = date.split("-")
        if len(parts) == 3 and all(p.isdigit() for p in parts):
            return date
        print("❌ Invalid date format.")
