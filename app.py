from flask import Flask

# create the Flask application
app = Flask(__name__)

@app.route("/", methods=["GET"])
def list_cars():
    # really bad idea in production, but ok for now
        return "Hello, world!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
