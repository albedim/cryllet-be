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
    def signin(cls, email, password) -> User:
        user: User = sql.session.query(User).filter(User.email == email).filter(User.password == password).first()
        return user

    @classmethod
    def signup(cls, username, email, password) -> None:
        user: User = User(username, email, password)
        sql.session.add(user)
        sql.session.commit()

    @classmethod
    def getUserById(cls, userId) -> User:
        user: User = sql.session.query(User).filter(User.user_id == userId).first()
        return user

    @classmethod
    def getUserByEmail(cls, email) -> User:
        user: User = sql.session.query(User).filter(User.email == email).first()
        return user

    @classmethod
    def getUserByUsername(cls, username) -> User:
        user: User = sql.session.query(User).filter(User.username == username).first()
        return user

    @classmethod
    def createForgottenPasswordToken(cls, user, token) -> None:
        user.password_forgotten_token = token
        sql.session.commit()

    @classmethod
    def getUserByPasswordForgottenToken(cls, token) -> User:
        user: User = sql.session.query(User).filter(User.password_forgotten_token == token).first()
        return user