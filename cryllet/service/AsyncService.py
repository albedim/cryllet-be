import base64
import datetime
import io
from datetime import timedelta
from typing import Any, Tuple

from flask import Response
from flask_jwt_extended import create_access_token

from cryllet.configuration.config import app
from cryllet.model.entity.User import User
from cryllet.model.repository.UserRepository import UserRepository
from cryllet.utils.Constants import Constants
from cryllet.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/05/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the async service
#

class AsyncService():

    @classmethod
    def checkExpiration(cls):
        with app.app_context():
            users: list[User] = UserRepository.getAllUsers()
            for user in users:
                if user.premium:
                    if user.expires_on == datetime.date.today():
                        Utils.sendExpireEmail(user)
                        UserRepository.setExpired(user)


