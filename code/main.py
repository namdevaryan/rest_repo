from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)


# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(10), nullable=False)

    def __init__(self, name, age, grade): # Add constructor
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, grade='{self.grade}')"


# Create the database tables
with app.app_context():
    db.create_all()

# Routes for CRUD operations


@app.route('/favicon.ico')
def favicon():
    return '', 204


@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Student API",
        "endpoints": {
            "GET /students": "Get all students",
            "GET /students/<id>": "Get a specific student",
            "POST /students": "Add a new student",
            "PUT /students/<id>": "Update a student",
            "DELETE /students/<id>": "Delete a student"
        }
    })


# 1. Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ['name', 'age', 'grade']):
            return jsonify({"error": "Missing required fields"}), 400
        
        if not isinstance(data['name'], str) or not isinstance(data['age'], int) or not isinstance(data['grade'], str):
            return jsonify({"error": "Invalid data types"}), 400
            
        if data['age'] < 0 or data['age'] > 150:
            return jsonify({"error": "Invalid age"}), 400
            
        new_student = Student(name=data['name'], age=data['age'], grade=data['grade'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"message": "Student added successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# 2. Get all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    student_list = []
    for student in students:
        student_list.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "grade": student.grade
        })
    return jsonify(student_list), 200


# 3. Get a student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "grade": student.grade
    }), 200


# 4. Update a student's information
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    try:
        student = Student.query.get_or_404(id)
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        if 'age' in data and (not isinstance(data['age'], int) or data['age'] < 0 or data['age'] > 150):
            return jsonify({"error": "Invalid age"}), 400
            
        student.name = data.get('name', student.name)
        student.age = data.get('age', student.age)
        student.grade = data.get('grade', student.grade)
        
        db.session.commit()
        return jsonify({"message": "Student updated successfully!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# 5. Delete a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    try:
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        return jsonify({"message": "Student deleted successfully!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
