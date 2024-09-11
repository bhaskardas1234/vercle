from flask import Flask,jsonify
app=Flask(__name__)
@app.route('/',methods=['post'])
def welcome():
    return  jsonify({"status":"success"}),200

if __name__=="__main__":
    app.run(debug=True)