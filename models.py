from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db= SQLAlchemy()

class Employee(db.Model):
    __tablename__ = "Employee"

    id = db.Column(db.Integer, primary_key=True)

    employee_id=db.Column(db.Integer(),unique=True)

    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String())

    def __init__(self, employee_id, name, age, position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
     return f"{self.name}:{self.employee_id}"
