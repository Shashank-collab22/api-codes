from flask import Flask, jsonify, request


app = Flask(__name__)
students = {
    1: {"name": "Alice", "age": 20, "course": "Python"},
    2: {"name": "Bob", "age": 22, "course": "Flask"}
}
@app.route("/students",methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/students/<int:id>",methods=["GET"])
def get_student_Id(id):
    if id in students:
        return jsonify(students[id])
    return jsonify({"error": "Student not found"})

@app.route("/students",methods=["POST"])
def Create_Student():
    data = request.json
    next_id= max(students.keys())+1 if students else 1

    students[next_id]= {"name": data["name"], "age": data["age"], "course": data["course"]}
    return jsonify(students[next_id])

@app.route("/students/<int:id>,",methods=["DELETE]"])
def delete_Student(id):
    if id in students:
        del students[id]
        return jsonify(students)
    return jsonify({"error": "Student not found"})

if __name__ == "__main__":
    app.run(debug=True)