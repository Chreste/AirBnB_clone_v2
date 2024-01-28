#!/usr/bin/python3
" Sript that starts a Flask web application "

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    " function to return Hello HBNB! "
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    " function to return hbnb! "
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
   " Function to display 'C ' followed by the text variable (replacing underscores with spaces) "
   
   return "C {}".format(text.replace("_", " "))

if __name__ == "__main__":
    app.run(host='1.0.0.0', port=5000)
