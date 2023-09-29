import sqlite3

def create_students_table():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            student_name TEXT,
            student_email TEXT,
            student_department TEXT,
            student_year TEXT,
            password TEXT
        )
    ''')

    connection.commit()
    connection.close()

# Call the function to create the table
create_students_table()
