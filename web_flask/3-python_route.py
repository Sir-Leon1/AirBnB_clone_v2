#!/usr/bin/python3
"""
This module contains a Flask application with various routes demonstrating
different URL patterns and functionalities, including rendering templates
and handling dynamic URLs.

"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Route that returns 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route that returns 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Route that returns 'C <text>' with underscores replaced by spaces.

    Args:
        text (str): The text to display.

    Returns:
        str: Formatted string with underscores replaced by spaces.
    """
    return f"C {text.replace('_', ' ')}"


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Route that returns 'Python <text>' with underscores replaced by spaces.

    Args:
        text (str): The text to display.

    Returns:
        str: Formatted string with underscores replaced by spaces.
    """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Route that returns '<n> is a number' if n is an integer.

    Args:
        n (int): The number to display.

    Returns:
        str: String indicating the number is a number.
    """
    return f"{n} is a number"


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    """Route that renders a template with n passed as a variable.

    Args:
        n (int): The number to pass to the template.

    Returns:
        str: Rendered template with the number.
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Route that renders a template indicating if n is odd or even.

    Args:
        n (int): The number to evaluate.

    Returns:
        str: Rendered template indicating if the number is odd or even.
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
