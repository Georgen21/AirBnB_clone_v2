#!/usr/bin/python3
""" Starts Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Print Web """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Print Web """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """print C followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
