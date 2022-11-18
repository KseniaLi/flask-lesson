from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Simple flask app</h1>"

if __name__ == "main":
    app.run(host='0.0.0.0', port=5000, debug=True)
