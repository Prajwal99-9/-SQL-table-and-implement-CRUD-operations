# Import the MySQL connector library
import mysql.connector

# Create a connection object to connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost", # The host name or IP address of the MySQL server
    user="root", # The user name for the MySQL server
    password="Best@8217", # The password for the MySQL server
    database="test" # The name of the database to use
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the Registration table with the given fields
cursor.execute("""
CREATE TABLE Registration (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    DateOfBirth DATE,
    Phone VARCHAR(15), # An additional field for phone number
    UNIQUE (Email) # A constraint to ensure email is unique
)
""")

# Commit the changes to the database
conn.commit()

# Define a function to create a new record in the Registration table
def create_record(name, email, date_of_birth, phone):
    # Prepare the SQL query with placeholders for the values
    query = "INSERT INTO Registration (Name, Email, DateOfBirth, Phone) VALUES (%s, %s, %s, %s)"
    # Execute the query with the given values
    cursor.execute(query, (name, email, date_of_birth, phone))
    # Commit the changes to the database
    conn.commit()
    # Return the ID of the inserted record
    return cursor.lastrowid

# Define a function to retrieve a record from the Registration table by ID
def read_record_by_id(id):
    # Prepare the SQL query with a placeholder for the ID
    query = "SELECT * FROM Registration WHERE ID = %s"
    # Execute the query with the given ID
    cursor.execute(query, (id,))
    # Fetch the result as a tuple
    result = cursor.fetchone()
    # Return the result or None if not found
    return result

# Define a function to update a record in the Registration table by ID
def update_record_by_id(id, name, email, date_of_birth, phone):
    # Prepare the SQL query with placeholders for the values and the ID
    query = "UPDATE Registration SET Name = %s, Email = %s, DateOfBirth = %s, Phone = %s WHERE ID = %s"
    # Execute the query with the given values and ID
    cursor.execute(query, (name, email, date_of_birth, phone, id))
    # Commit the changes to the database
    conn.commit()
    # Return the number of affected rows
    return cursor.rowcount

# Define a function to delete a record from the Registration table by ID
def delete_record_by_id(id):
    # Prepare the SQL query with a placeholder for the ID
    query = "DELETE FROM Registration WHERE ID = %s"
    # Execute the query with the given ID
    cursor.execute(query, (id,))
    # Commit the changes to the database
    conn.commit()
    # Return the number of affected rows
    return cursor.rowcount

# Test the functions with some sample data
# Create a new record
id = create_record("Prajwal", "kumbar@example.com", "2001-01-01", "9900306938")
print(f"Created a new record with ID {id}")

# Retrieve the record by ID
record = read_record_by_id(id)
print(f"Retrieved the record by ID {id}: {record}")

# Update the record by ID
rows = update_record_by_id(id, "Alice", "alice@gmail.com", "1990-01-01", "0987654321")
print(f"Updated the record by ID {id}: {rows} row(s) affected")

# Delete the record by ID
rows = delete_record_by_id(id)
print(f"Deleted the record by ID {id}: {rows} row(s) affected")

# Close the cursor and the connection
cursor.close()
conn.close()
