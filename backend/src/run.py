"""
Script to start running the server
"""

from os import getenv
from server import server

if __name__ == "__main__":
    server.run(
        host=getenv("HOST"),
        port=getenv("PORT"),
        debug=getenv("DEBUG")=="1"
    )
