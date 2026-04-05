from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

students = []

@app.route("/add-student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")

        if not name or not age:
            return "Missing fields", 400

        student = {"name": name, "age": age}
        students.append(student)

        return f"Student {name} added successfully!", 200

    return render_template("add-student.html")


@app.route("/")
def get_student():
    return jsonify(students)


if __name__ == "__main__":
    app.run(debug=True)