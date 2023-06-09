from db import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    signup_date = db.Column(db.Date)
    total_experiments = db.Column(db.Integer)
    most_common_compounds_ids = db.Column(db.ARRAY(db.Integer))


class Compound(db.Model):
    __tablename__ = "compounds"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    structure = db.Column(db.String(128))


class GlobalStatistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    average_experiments = db.Column(db.Float)
