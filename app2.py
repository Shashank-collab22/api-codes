from flask import Flask, jsonify
from pymongo import MongoClient
import certifi

app = Flask(__name__)

# Use your own MongoDB URI here
MONGO_URI = "mongodb+srv://shashankkotagiri22_db_user:<Shashank22012003>@cluster0.ep0ktwn.mongodb.net/?appName=Cluster0"

# Use certifi to fix SSL certificate verification
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client['school']
students_collection = db['students']

def format_student(student):
    return {
        "id": str(student.get("_id")),
        "name": student.get("name"),
        "age": student.get("age"),
        "course": student.get("course")
    }

@app.route('/students', methods=['GET'])
def get_students():
    students_list = [format_student(s) for s in students_collection.find()]
    return jsonify(students_list)

@app.route('/students/<id>', methods=['GET'])
def get_student(id):
    student = students_collection.find_one({"_id": id})
    if student:
        return jsonify(format_student(student))
    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)