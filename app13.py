from flask import Flask,jsonify ,request

app = Flask(__name__)
@app.route("/analyze/<int:id>",methods=["POST","GET"])
def analyze(id):
    number=id
    is_even=id%2==0
    square=id**2
    return jsonify(number=number,is_even=is_even,square=square)
if __name__=="__main__":
    app.run(debug=True)
