import sqlite3

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))

    result = cursor.fetchone()
    conn.close()

    return result

user = input("Enter username: ")
pwd = input("Enter password: ")

if login(user, pwd):
    print("Login successful")
else:
    print("Invalid login")
