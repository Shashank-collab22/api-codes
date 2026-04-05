from flask import Flask,jsonify,request
app = Flask(__name__)
health={
  "status": "running",
  "version": "1.0"
}
@app.route("/health",methods=['GET'])
def health():
    return jsonify(health,)
if __name__ == "__main__":
    app.run(debug=True)