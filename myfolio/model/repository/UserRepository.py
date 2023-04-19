from myfolio.configuration.config import sql
from myfolio.model.entity.User import User


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 18/04/23
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
    def signup(cls, birthday, firstName, lastName, email, username, password, introduction, image) -> None:
        user: User = User(firstName, lastName, email, username, password, introduction, birthday, image)
        sql.session.add(user)
        sql.session.commit()

    @classmethod
    def getUserById(cls, userId) -> User:
        user: User = sql.session.query(User).filter(User.user_id == userId).first()
        return user

    @classmethod
    def getUserByEmail(cls, email):
        user: User = sql.session.query(User).filter(User.email == email).first()
        return user

    @classmethod
    def getUserByUsername(cls, username):
        user: User = sql.session.query(User).filter(User.username == username).first()
        return user

    @classmethod
    def createForgottenPasswordToken(cls, user, token):
        user.password_forgotten_token = token
        sql.session.commit()

    @classmethod
    def getUserByPasswordForgottenToken(cls, token):
        user: User = sql.session.query(User).filter(User.password_forgotten_token == token).first()
        return user

    @classmethod
    def changePassword(cls, userId, newPassword):
        user: User = cls.getUserById(userId)
        user.password = newPassword
        sql.session.commit()

    @classmethod
    def change(cls, user, name, minecraftUsername, email):
        user.name = name
        user.minecraft_username = minecraftUsername
        user.email = email
        sql.session.commit()

    @classmethod
    def changeIntroduction(cls, userId, newIntroduction):
        user: User = cls.getUserById(userId)
        user.introduction = newIntroduction
        sql.session.commit()
