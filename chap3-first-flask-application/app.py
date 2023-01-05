"""Flask Application for Paws Rescue Center."""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def homepage():
    """View function for Home Page."""
    return "Paws Rescue Center 🐾"

@app.route("/about")
def about():
    """View function for About Page."""
    return """We are a non-profit organization working as an animal rescue center. 
    We aim to help you connect with the purrfect furbaby for you! 
    The animals you find at our website are rescue animals which have been rehabilitated. 
    Our mission is to promote the ideology of "Adopt, don't Shop"! """


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
