from flask import Flask
from flask_cors import CORS

from models import db
from resources import create_api
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    api = create_api()
    api.init_app(app)
    db.init_app(app)

    # 解决跨域问题
    CORS(app)
    return app

