from flask import Flask, render_template, request, redirect, url_for
try:
    from .db import db, Student
except ImportError:
    from db import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/student_registration'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        student = Student(name=name, age=age, email=email)
        db.session.add(student)
        db.session.commit()

        # Redirect to the 'students' page after successful registration
        return redirect(url_for('students'))

    return render_template('register.html')

@app.route('/students')
def students():
    # Fetch all students from the database
    all_students = Student.query.all()
    return render_template('students.html', students=all_students)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create all the database tables
    app.run(host='0.0.0.0', debug=True)
