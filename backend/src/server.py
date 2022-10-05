"""
Main file for Flask server configuration
"""

# Flask imports
from flask import Flask
from flask_cors import CORS

# Create server
server = Flask(__name__)
CORS(server)

# Test route
@server.route("/", methods=["GET"])
def root():
    """
    Test route to check if the server is running.
    """
    return "Hello World!"
