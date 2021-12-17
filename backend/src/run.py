from logging import debug
from server import server
from os import getenv

if __name__ == "__main__":
    debug = getenv("DEBUG") == "1"
    server.run(host=getenv("HOST"), port=getenv("PORT"), debug=debug)
