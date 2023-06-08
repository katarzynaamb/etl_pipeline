import os

from flask import Flask
from flask_migrate import Migrate

from db import db
from etl import etl


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ.get("APP_SETTINGS","config.Config"))
    db.init_app(app)
    Migrate(app, db)

    # Your API that can be called to trigger your ETL process
    @app.route("/etl/trigger", methods=["POST"])
    def trigger_etl():
        # Trigger your ETL process here
        etl()
        return {"message": f"ETL process started"}, 200

    @app.route("/")
    def home():
        return "ETL pipeline app", 200

    return app
