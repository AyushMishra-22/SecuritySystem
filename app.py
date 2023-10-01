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

@app.route('/employee_details')
def employee_details():
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM employee')
        employees = cursor.fetchall()

    return render_template("EmplyeeDetails.html", employees=employees)

@app.route('/student_details')
def student_details():
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()   

    return render_template("StudentsDetails.html", students = students)

@app.route('/submit_employee_registration', methods=['POST'])
def submit_employee_registration():
    employee_id = request.form['employee_id']
    employee_name = request.form['employee_name']
    employee_email = request.form['employee_email']
    employee_department = request.form['employee_department']
    employee_designation = request.form['employee_designation']
    employee_password = request.form['employee_password']
    employee_image = request.form['employee_image']
    
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO employee (employee_id, employee_name, employee_email, employee_department, employee_designation, employee_password, employee_image)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (employee_id, employee_name, employee_email, employee_department, employee_designation, employee_password, employee_image))
        connection.commit()
    return render_template("EmployeeLogin.html")

@app.route('/submit_student_registration', methods=['POST'])
def submit_student_registration():
    student_id = request.form['student_id']
    student_name = request.form['student_name']
    student_email = request.form['student_email']
    student_department = request.form['student_department']
    student_year = request.form['student_year']
    password = request.form['student_password']
    student_image = request.form['student_image']

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO students (student_id, student_name, student_email, student_department,student_year, password, student_image)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (student_id, student_name, student_email, student_department,student_year, password, student_image))
        connection.commit()

    return render_template("StudentsLogin.html")

@app.route('/submit_employee_login', methods=['POST'])
def submit_employee_login():
    employee_id = request.form['employee_id']
    employee_password = request.form['employee_password']

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT employee_id FROM employee WHERE employee_id = ? AND employee_password = ?;
        ''', (employee_id, employee_password))

        result = cursor.fetchone()

    if result:
        return redirect(url_for('employee_details'))
    else:
        return render_template("EmployeeLogin.html", error_message="Invalid credentials")

@app.route('/submit_student_login', methods=['POST'])
def submit_student_login():
    student_email = request.form['student_email']
    student_password = request.form['student_password']

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT student_email FROM students WHERE student_email = ? AND password = ?;
        ''', (student_email, student_password))

        result = cursor.fetchone()

    if result:
        return redirect(url_for('student_details'))
    else:
        return render_template("StudentsLogin.html", error_message="Invalid credentials")



if __name__ == "__main__":
    app.run(debug=True)

    