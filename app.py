from flask import Flask, render_template, request, redirect, url_for

from db import connect_db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/students_login')
def students_login():
    return render_template('StudentsLogin.html')



@app.route('/employee_login')
def employee_login():
    return render_template('EmployeeLogin.html')

@app.route('/students_registration')
def students_registration():
    return render_template('StudentsRegistration.html')

@app.route('/employee_registration')
def employee_registration():
    return render_template('EmployeeRegistration.html')

@app.route('/submit_student_registration', methods=['POST'])
def submit_student_registration():
    student_name = request.form['student_name']
    student_email = request.form['student_email']
    student_department = request.form['student_department']
    student_year = request.form['student_year']
    password = request.form['student_password']

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO students (student_name, student_email, student_department,student_year, password)
            VALUES (?, ?, ?, ?,?)
        ''', (student_name, student_email, student_department,student_year, password))
        connection.commit()

    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)

    