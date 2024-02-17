#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask

app = Flask(__name__)

# Define route for the root url '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB! """
    return "Hello HBNB!"


if __name__ == "__main__":
    # Start the Flask development server
    # Listen to available network interfaces (0.0.0.0) and port 5000
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
