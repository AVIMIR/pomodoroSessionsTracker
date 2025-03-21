import tkinter
import psycopg2 

# CREATE TABLE sessions (
#     id SERIAL PRIMARY KEY AUTOINCREMENT,
#     tdate DATE,
#     amount INT,
#     first_time TIME,
#     last_time TIME,
# );

connection = psycopg2.connect(
    dbname="sessions",
    user="pomodoro",
    password="1",
)


cursor = connection.cursor()

cursor.execute("""
    SELECT * FROM sessions;
""")

lines = cursor.fetchall()

for line in lines:
    print(line)
print("OK")