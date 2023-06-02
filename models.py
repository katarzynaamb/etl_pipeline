from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    signup_date = db.Column(db.Date)
    total_experiments = db.Column(db.Integer)
    most_common_compound_name = db.Column(db.String(128))
    most_common_compound_structure = db.Column(db.String(128))


class GlobalStatistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    average_experiments = db.Column(db.Integer)
