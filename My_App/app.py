import sqlite3
from datetime import datetime

# Connect to the SQLite database (you can change this to another database if needed)
conn = sqlite3.connect('registration.db')
cursor = conn.cursor()

# Create Registration table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS Register (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    DateOfBirth DATE
);
''')
conn.commit()

# CRUD Operations

def create_record(name, email, date_of_birth):
    try:
        cursor.execute('''
        INSERT INTO Register (Name, Email, DateOfBirth)
        VALUES (?, ?, ?);
        ''', (name, email, date_of_birth))
        conn.commit()
        print("Record created successfully.")
    except Exception as e:
        print(f"Error creating record: {e}")

def read_records():
    try:
        cursor.execute('SELECT * FROM Register;')
        records = cursor.fetchall()
        if records:
            for record in records:
                print(record)
        else:
            print("No records found.")
    except Exception as e:
        print(f"Error reading records: {e}")

def update_record(record_id, new_name, new_email, new_date_of_birth):
    try:
        cursor.execute('''
        UPDATE Register
        SET Name=?, Email=?, DateOfBirth=?
        WHERE ID=?;
        ''', (new_name, new_email, new_date_of_birth, record_id))
        conn.commit()
        print("Record updated successfully.")
    except Exception as e:
        print(f"Error updating record: {e}")

def delete_record(record_id):
    try:
        cursor.execute('DELETE FROM Register WHERE ID=?;', (record_id,))
        conn.commit()
        print("Record deleted successfully.")
    except Exception as e:
        print(f"Error deleting record: {e}")

# Example Usage
create_record("shashi kumar", "shashi@example.com", datetime(2000, 5, 10))
create_record("Rahul hugar", "sachin@example.com", datetime(1999, 7, 16))

read_records()

update_record(1, "John Updated", "Rahul.updated@example.com", datetime(1992, 2, 20))

read_records()

delete_record(2)

read_records()

# Close the database connection
conn.close()
