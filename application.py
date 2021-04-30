from flask import Flask

from routes import trie_blueprint
from models import db, init_db

import os.path

application = Flask(__name__)
application.config.update(
    SQLALCHEMY_DATABASE_URI='sqlite:///production.db',
    DEBUG=True,
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
db.init_app(application)

application.register_blueprint(trie_blueprint)

if __name__ == "__main__":
    if not os.path.isfile("production.db"):
        with application.app_context():
            init_db()
    application.debug = True
    application.run()
