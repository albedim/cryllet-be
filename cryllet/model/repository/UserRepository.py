import datetime

from sqlalchemy.sql.elements import or_

from cryllet.configuration.config import sql
from cryllet.model.entity.User import User


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/05/23
# Created at: 19:35
# Version: 1.0.0
# Description: This is the class for the user repository
#

class UserRepository():

    @classmethod
    def signinEmail(cls, email, password) -> User:
        user: User = sql.session.query(User).filter(or_(
            ((User.email == email) & (User.password == password)),
            ((User.username == email) & (User.password == password))
        )).first()
        return user

    @classmethod
    def signinUsername(cls, username, password) -> User:
        user: User = sql.session.query(User).filter(User.username == username).filter(User.password == password).first()
        return user

    @classmethod
    def signup(cls, username, email, password) -> User:
        user: User = User(username, email, password)
        sql.session.add(user)
        sql.session.commit()
        return user

    @classmethod
    def getUserById(cls, userId) -> User:
        user: User = sql.session.query(User).filter(User.user_id == userId).first()
        return user

    @classmethod
    def getUserByEmail(cls, email) -> User:
        user: User = sql.session.query(User).filter(User.email == email).first()
        return user

    @classmethod
    def getAllUsers(cls) -> list:
        users: list = sql.session.query(User).all()
        return users

    @classmethod
    def getUserByUsername(cls, username) -> User:
        user: User = sql.session.query(User).filter(User.username == username).first()
        return user

    @classmethod
    def createForgottenPasswordToken(cls, user, token) -> None:
        user.password_forget_token = token
        sql.session.commit()

    @classmethod
    def getUserByPasswordForgottenToken(cls, token) -> User:
        user: User = sql.session.query(User).filter(User.password_forget_token == token).first()
        return user

    @classmethod
    def changePassword(cls, userId, password) -> User:
        user: User = cls.getUserById(userId)
        user.password = password
        sql.session.commit()

    @classmethod
    def setExpired(cls, user) -> User:
        user.premium = False
        user.expires_on = None
        sql.session.commit()

    @classmethod
    def setSubscription(cls, user, date) -> User:
        user.premium = True
        user.expires_on = date
        sql.session.commit()
