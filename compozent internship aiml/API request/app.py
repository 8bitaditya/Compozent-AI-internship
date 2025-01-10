from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = [
    {'id': 1, 'name': 'Alice', 'age': 12, 'grade': 'A'},
    {'id': 2, 'name': 'Bob', 'age': 14, 'grade': 'B'},
    {'id': 3, 'name': 'Charlie', 'age': 13, 'grade': 'C'},
]

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/students', methods=['POST'])
def add_student():
    name = request.form.get('name')
    age = int(request.form.get('age'))
    grade = request.form.get('grade')
    new_student = {
        'id': len(students) + 1,
        'name': name,
        'age': age,
        'grade': grade
    }
    students.append(new_student)
    return redirect(url_for('index'))

@app.route('/students/<int:id>', methods=['POST'])
def update_student(id):
    name = request.form.get('name')
    age = int(request.form.get('age'))
    grade = request.form.get('grade')

    for student in students:
        if student['id'] == id:
            student['name'] = name
            student['age'] = age
            student['grade'] = grade
            break

    return redirect(url_for('index'))

@app.route('/students/delete/<int:id>', methods=['POST'])
def delete_student(id):
    global students
    students = [student for student in students if student['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)