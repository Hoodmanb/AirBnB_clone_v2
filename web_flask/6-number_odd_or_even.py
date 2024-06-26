#!/usr/bin/python3
""" a Script that display 'Hello HBNB!'
    using flask with / route
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ return 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return 'HBNB!' """
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ returns the passed parameter """
    return 'C {}'.format(text.replace('_', ' '))


@app.route("/python/", defaults={"text": "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ returns the passed parameter """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def nIsNum(n):
    """ returns the passed parameter """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ returns the passed parameter """
    return render_template('5-number.html', n=n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def odd_even(n):
    """ returns an html template  """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
