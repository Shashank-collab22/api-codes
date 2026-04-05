from flask import Flask,jsonify,request
app = Flask(__name__)
students={}
@app.route("/students",methods=["POST"])

def details():
    data= request.get_json()
    if not data:
        return jsonify({"error":"no data"}),400
    if "name" not in data or "age" not in data:
        return jsonify({"error":"no data"}),400
    name=data["name"]
    age=data["age"]
    next_id= max(students.keys(), default=0) + 1
    students[next_id]={"name":name,"age":age}
    return jsonify({"id":next_id,"students":students[next_id]}),201
@app.route("/students",methods=["GET"])
def list():
    return jsonify(students)
@app.route("/students/<int:id>",methods=["GET"])
def by_id(id):
    if id not in students:
        return jsonify({"error":"student not found"}),404
    return jsonify(students[id])
@app.route("/students/<int:id>",methods=["DELETE"])
def delete_Student(id):
    if id in students:
        del students[id]
        return "deleted successfully",200
    return jsonify({"error": "Student not found"}),404
@app.route("/students/<int:id>",methods=["PUT"])
def update_Student(id):
    if id in students:
        students[id] = request.json
        return "updated successfully",200
    return jsonify({"error": "Student not found"}),404
@app.route("/students/search", methods=["GET"])
def search_by_name():
    name = request.args.get("name")

    if not name:
        return jsonify({"error": "name is required"}), 400

    results = {}

    for id, student in students.items():
        if student["name"].lower() == name.lower():
            results[id] = student

    if not results:
        return jsonify({"error": "student not found"}), 404

    return jsonify(results), 200

@app.route("/students/filter",methods=["GET"])
def filter_by_age():
    age = request.args.get("min_age")
    if not age:
        return jsonify({"error": "min_age is required"}), 404

    try:
        min_age = int(age)
    except ValueError:
        return jsonify({"error": "min_age is required"}), 400

    results = {}
    for id, student in students.items():
        if student["age"] > min_age:
            results[id] = student
    return jsonify(results), 200




if __name__ == "__main__":
    app.run(debug=True)
