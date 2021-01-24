from flask_restful_swagger import swagger

from extensions import db


@swagger.model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    level_id = db.Column(db.ForeignKey('level.id'), nullable=True)
    level = db.relationship('Level', back_populates='user', uselist=False, foreign_keys=[level_id])


@swagger.model
class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)
    user = db.relationship('User', back_populates='level')
