from flask import Flask, jsonify,request, make_response


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/login', methods = ["GET", "POST"])
def login():
    form = request.form
    print(form)
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)