from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route("/add",methods=["POST"])
def addition():
    add =request.get_json()
    if not add:
        return jsonify({"message":"No data"}),400
    if 'a' not in add or 'b' not in  add:
        return jsonify({"eror":"both a and b are required"}),400
    a=add['a']
    b=add['b']
    result=a+b
    return jsonify({"result":result})
if __name__=="__main__":
    app.run(debug=True)