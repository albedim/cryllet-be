import base64
import datetime
import io
from datetime import timedelta
from typing import Any, Tuple

from dateutil.relativedelta import relativedelta
from flask import Response
from flask_jwt_extended import create_access_token
from cryllet.model.entity.User import User
from cryllet.model.repository.UserRepository import UserRepository
from cryllet.utils.Constants import Constants
from cryllet.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/05/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user service
#

class UserService():

    @classmethod
    def signin(cls, request: dict) -> tuple[Any, int] | Any:
        try:
            user: User = UserRepository.signin(
                request['email_username'],
                Utils.hash(request['password'])
            )
            if user is not None:
                return Utils.createSuccessResponse(True, {
                    "token": create_access_token(
                        identity=user.toJson(),
                        expires_delta=timedelta(weeks=4))
                })
            else:
                return Utils.createWrongResponse(False, Constants.USER_NOT_FOUND, 404), 404
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def existsByEmail(cls, email) -> bool:
        return UserRepository.getUserByEmail(email) is not None

    @classmethod
    def existsByUsername(cls, username) -> bool:
        return UserRepository.getUserByUsername(username) is not None

    @classmethod
    def getUserById(cls, userId):
        user: User = UserRepository.getUserById(userId)
        if user is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            return user.toJson()

    @classmethod
    def signup(cls, request: dict):
        try:
            if cls.existsByEmail(request['email']):
                return Utils.createWrongResponse(False, Constants.ALREADY_CREATED, 409), 409
            else:
                user: User = UserRepository.signup(
                    request['username'],
                    request['email'],
                    Utils.hash(request['password']),
                )
                if request['promo_code'] in Constants.PROMO_CODES:
                    cls.setSubscription(user.user_id)
                return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def createForgottenPasswordToken(cls, email):
        user: User = UserRepository.getUserByEmail(email)
        if user is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            token: str = Utils.createLink(40)
            UserRepository.createForgottenPasswordToken(user, token)
            Utils.sendPasswordForgottenEmail(user.email, token)
            return Utils.createSuccessResponse(True, Constants.CREATED), 200

    @classmethod
    def getUserByPasswordForgottenToken(cls, token):
        user: User = UserRepository.getUserByPasswordForgottenToken(token)
        if user is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            return Utils.createSuccessResponse(True, user.user_id), 200

    @classmethod
    def checkUsername(cls, username) -> tuple[Any, int] | dict:
        if cls.existsByUsername(username):
            return Utils.createWrongResponse(False, Constants.ALREADY_CREATED, 409), 409
        else:
            return Utils.createSuccessResponse(True, None)

    @classmethod
    def changePassword(cls, request) -> tuple[Any, int] | dict:
        UserRepository.changePassword(request['user_id'], Utils.hash(request['new_password']))
        return Utils.createSuccessResponse(True, Constants.CREATED)

    @classmethod
    def setSubscription(cls, userId) -> tuple[Any, int] | dict:
        user: User = UserRepository.getUserById(userId)
        if user.premium:
            return Utils.createWrongResponse(False, Constants.ALREADY_CREATED, 409), 409
        else:
            expiresOn = datetime.date.today() + relativedelta(months=1)
            UserRepository.setSubscription(user, expiresOn)
            return Utils.createSuccessResponse(True, Constants.CREATED)

    @classmethod
    def sync(cls, requestUser):
        user = cls.getUserById(requestUser['user_id'])
        if user == requestUser:
            return Utils.createSuccessResponse(True, Constants.UP_TO_DATE)
        else:
            return Utils.createSuccessResponse(False, user)


