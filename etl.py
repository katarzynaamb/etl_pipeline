from collections import Counter

import pandas

from db import db
from models import User, Compound, GlobalStatistics

USERS_FILE_PATH = "data/users.csv"
USER_EXPERIMENTS_FILE_PATH = "data/user_experiments.csv"
COMPOUNDS_FILE_PATH = "data/compounds.csv"


def save_compound(row):
    compound = Compound.query.get(row["compound_id"])

    # Update existing compound or create a new one
    if compound:
        compound.name = row["compound_name"],
        compound.structure = row["compound_structure"],
    else:
        compound = Compound(
            id=row["compound_id"],
            name=row["compound_name"],
            structure=row["compound_structure"]
        )
    db.session.add(compound)


def save_user(row):
    user = User.query.get(row["user_id"])

    # Update existing user or create a new one
    if user:
        user.name = row["name"],
        user.email = row["email"],
        user.signup_date = row["signup_date"],
        user.total_experiments = row["total_experiments"]
    else:
        user = User(
            id=row["user_id"],
            name=row["name"],
            email=row["email"],
            signup_date=row["signup_date"],
            total_experiments=row["total_experiments"]
        )

    # in case of a tie there are multiple most common compounds
    list_of_compounds = row["experiment_compound_ids"].split(";")
    counter = Counter(list_of_compounds)
    num_of_occurrences_of_most_common_compound = max(counter.values())
    all_most_common_compounds = [k for k, v in counter.items() if v == num_of_occurrences_of_most_common_compound]

    user.most_common_compounds_ids = all_most_common_compounds

    db.session.add(user)


def save_global_statistics(users_with_features):
    number_of_users = len(users_with_features.index)
    total_experiments = users_with_features["total_experiments"].sum()
    num_of_experiments_per_user = total_experiments / number_of_users

    global_statistics = GlobalStatistics.query.get(1)
    if global_statistics:
        global_statistics.average_experiments = num_of_experiments_per_user
    else:
        global_statistics = GlobalStatistics(
            average_experiments=num_of_experiments_per_user
        )
    db.session.add(global_statistics)


def etl():
    # Load CSV files
    users = pandas.read_csv(USERS_FILE_PATH, sep=",\s+", engine="python")
    user_experiments = pandas.read_csv(USER_EXPERIMENTS_FILE_PATH, sep=",\s+", engine="python")
    compounds = pandas.read_csv(COMPOUNDS_FILE_PATH, sep=",\s+", engine="python")

    # Process files to derive features
    users_with_experiments = users.filter(["user_id"]).merge(user_experiments, on="user_id")
    num_of_experiments_per_user = users_with_experiments.groupby(["user_id"]).size().reset_index(
        name="total_experiments"
    )

    users_compounds = users_with_experiments.groupby(["user_id"])["experiment_compound_ids"].apply(
        lambda column: ';'.join(column)
    ).reset_index()

    users_with_features = users.merge(users_compounds, on="user_id").merge(num_of_experiments_per_user, on="user_id")

    # Upload processed data into a database
    users_with_features.apply(lambda row: save_user(row), axis=1)
    compounds.apply(lambda row: save_compound(row), axis=1)
    save_global_statistics(users_with_features)

    db.session.commit()
