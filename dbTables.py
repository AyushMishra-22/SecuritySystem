import sqlite3

def create_students_table():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            student_name TEXT,
            student_email TEXT,
            student_department TEXT,
            student_year TEXT,
            password TEXT,
            student_image BLOB
        )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee (
        employee_id TEXT PRIMARY KEY,
        employee_name TEXT,
        employee_email TEXT,
        employee_department TEXT,
        employee_designation TEXT,
        employee_password TEXT,
        employee_image BLOB
        )
    ''')

    connection.commit()
    connection.close()

# Call the function to create the table
create_students_table()
