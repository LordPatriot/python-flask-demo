from flask import Flask
import random

# create the Flask application
app = Flask(__name__)
quotes = []


def loadQuotes():
    file = open("quotes.txt", "r")
    for line in file:
        line = line.rstrip()
        if not line:
            break
        quotes.append(line.split("\t"))


@app.route("/", methods=["GET"])
def get_random_quote():
    n = len(quotes)
    r = random.randint(0, n - 1)
    return quotes[r][1]


if __name__ == "__main__":
    loadQuotes()
    app.run(host='0.0.0.0')
