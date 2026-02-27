"""
Fuck it
"""
import os
from flask import Flask
from routes.tracking import bpTracking
from routes.users import bpUsers

def create_app():
    """
    Creates flask app.
    """
    # creates flask app
    app = Flask(__name__)

    # define tracking blueprints url
    app.register_blueprint(bpTracking)
    app.register_blueprint(bpUsers)

    return app

if __name__ == "__main__":
    # starts flask app
    _app = create_app()
    port = int(os.environ.get("PORT", 5000))
    _app.run(host = '0.0.0.0', port = port, debug = True)
