"""Seed database with sample data from CSV files."""

from csv import DictReader
from app import db, User

db.drop_all()
db.create_all()

with open('generator/users.csv') as users:
    db.session.bulk_insert_mappings(User, DictReader(users))

db.session.commit()
