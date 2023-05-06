import datetime

from cryllet.configuration.config import sql
from cryllet.utils.Constants import Constants


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/05/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user entity
#


class User(sql.Model):
    __tablename__ = 'users'
    user_id: int = sql.Column(sql.Integer, primary_key=True)
    username: str = sql.Column(sql.String(20), nullable=False)
    email: str = sql.Column(sql.String(40), nullable=False)
    password: str = sql.Column(sql.String(40), nullable=False)
    premium: bool = sql.Column(sql.Boolean, nullable=False)

    def __init__(self, username, email, password):
        self.email = email
        self.password = password
        self.username = username
        self.premium = False

    def toJson(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'username': self.username,
            'premium': self.premium,
        }