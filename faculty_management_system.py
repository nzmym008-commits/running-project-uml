
import sqlite3

# ---------- Database Setup ----------
def setup_database():
    conn = sqlite3.connect("faculty.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        role TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS faculty (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        department TEXT
    )
    """)

    cursor.execute("SELECT * FROM users WHERE username='admin'")
    if cursor.fetchone() is None:
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            ("admin", "1234", "admin")
        )

    conn.commit()
    conn.close()

# ---------- Login Use Case ----------
def login():
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    conn = sqlite3.connect("faculty.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        print("Login successful")
        return True
    else:
        print("Invalid username or password")
        return False

# ---------- Add Faculty Member Use Case ----------
def add_faculty_member():
    print("\n--- Add Faculty Member ---")
    name = input("Faculty Name: ")
    email = input("Email: ")
    department = input("Department: ")

    conn = sqlite3.connect("faculty.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO faculty (name, email, department) VALUES (?, ?, ?)",
        (name, email, department)
    )

    conn.commit()
    conn.close()

    print("Faculty member added successfully")

# ---------- Main Program ----------
def main():
    print("Faculty Management System")
    setup_database()

    if login():
        add_faculty_member()
    else:
        print("Access denied")

if __name__ == "__main__":
    main()
