import os

from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
db = SQLAlchemy(app)
migrate = Migrate(app, db)


def etl():
    # Load CSV files
    # Process files to derive features
    # Upload processed data into a database
    pass


# Your API that can be called to trigger your ETL process
@app.route("/etl/trigger", methods=["POST"])
def trigger_etl():
    # Trigger your ETL process here
    etl()
    return {"message": f"ETL process started"}, 200


@app.route("/")
def home():
    return "ETL pipeline app", 200


if __name__ == '__main__':
    app.run(debug=True)
