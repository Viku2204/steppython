import sqlite3
import random
connect = sqlite3.connect("study.db")
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT,
    email TEXT
)
''')

first_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah', 'Ian', 'Julia']
last_names = ['Smith', 'Johnson', 'Lee', 'Patel', 'Kim', 'Brown', 'Wilson', 'Garcia', 'Martin', 'Lopez']
grades = ['7th', '8th', '9th', '10th', '11th', '12th']

for i in range(50):
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    name = f"{fname} {lname}"
    age = random.randint(13, 18)
    grade = random.choice(grades)
    email = f"{fname.lower()}.{lname.lower()}{i}@school.edu"

connect.commit()
connect.close()
