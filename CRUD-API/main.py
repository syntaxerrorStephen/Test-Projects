import sqlite3

# Connect to the database
conn = sqlite3.connect("users.db")
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, name text, email text)''')

def create_user(name, email):
  # Add a new user to the database
  c.execute("INSERT INTO users (name, email) VALUES (?,?)", (name, email))
  conn.commit()
  print(f"User '{name}' added to the database.")

def read_users():
  # Retrieve all users from the database
  c.execute("SELECT * FROM users")
  users = c.fetchall()
  return users

def update_user(id, name, email):
  # Update a user in the database
  c.execute("UPDATE users SET name=?, email=? WHERE id=?", (name, email, id))
  conn.commit()
  print(f"User with ID {id} updated in the database.")

def delete_user(id):
  # Delete a user from the database
  c.execute("DELETE FROM users WHERE id=?", (id,))
  conn.commit()
  print(f"User with ID {id} deleted from the database.")

# Test the CRUD API
create_user("John Smith", "john@example.com")
create_user("Jane Doe", "jane@example.com")
print(read_users())
update_user(1, "John Doe", "john.doe@example.com")
delete_user(2)
print(read_users())

# Close the connection to the database
conn.close()
