import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def insert(self):
        # conncetion = sqlite3.Connection('data.db')
        # cursor = conncetion.cursor()

        # insert_query = "insert into users values (NULL , ?, ? )"
        # cursor.execute(insert_query, (self.username, self.password))

        # conncetion.commit()
        # conncetion.close()
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        # connection = sqlite3.Connection('data.db')
        # cursor = connection.cursor()

        # find_by_id_query = "select * from users where id = ?"
        # result = cursor.execute(find_by_id_query, (_id,)).fetchone()
        # connection.close()

        # return cls(*result) if result else None
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_username(cls, username):
        # connection = sqlite3.Connection('data.db')
        # cursor = connection.cursor()

        # find_by_username_query = "select * from users where username = ?"
        # result = cursor.execute(find_by_username_query, (username,)).fetchone()
        # connection.close()

        # return cls(*result) if result else None

        return cls.query.filter_by(username=username).first()
