# app.py

from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    # This will look for 'index.html' in the 'templates' folder and display it.
    return render_template('index.html')

# This allows you to run the app directly from the command line
if __name__ == '__main__':
    # The host='0.0.0.0' makes it accessible on your local network
    # The port=5000 is the d0.0', port=5000, debug=True)
