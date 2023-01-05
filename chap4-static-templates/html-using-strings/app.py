"""Flask Application for Paws Rescue Center."""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def homepage():
    """View function for Home Page."""
    return "<h1 style='text-align: center;'>Paws Rescue Center 🐾</h1>"


@app.route("/about")
def about():
    """View function for About Page."""
    return """<h1>About Us:</h1><p>We are a non-profit organization working as an animal rescue.
    We aim to help you connect with purrfect furbaby for you!
    The animals you find at our website are rescued and rehabilitated animals.
    Our mission is to promote the ideology of "Adopt, don't Shop"!</p>"""


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
