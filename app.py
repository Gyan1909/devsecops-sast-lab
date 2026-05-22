import sqlite3

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)

    result = cursor.fetchone()
    conn.close()

    return result

user = input("Enter username: ")
pwd = input("Enter password: ")

if login(user, pwd):
    print("Login successful")
else:
    print("Invalid login")
