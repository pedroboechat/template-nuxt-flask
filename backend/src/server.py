"""
Implements a backend server
"""
# Imports
from flask import Flask

# Server instantiation and configuration
server = Flask(__name__)
server.config['JSON_SORT_KEYS'] = False


@server.get("/")
def root():
    """
    Simple route to check server status
    """
    return "OK"
