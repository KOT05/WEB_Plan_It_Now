import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("INSERT into users (name, email, hashed_password) VALUES (?, ?, ?)",
               ("Егор", "gev@mail.ru", "1"))

conn.commit()
conn.close()