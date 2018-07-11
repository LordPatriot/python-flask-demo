from flask import Flask

# create the Flask application
app = Flask(__name__)

@app.route("/", methods=["GET"])
def list_cars():
    return "Hello, world of 2018!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
