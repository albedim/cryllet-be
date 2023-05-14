import base64
import datetime
import io
from datetime import timedelta
from typing import Any, Tuple

from flask import Response
from flask_jwt_extended import create_access_token

from cryllet.configuration.config import app
from cryllet.model.entity.User import User
from cryllet.model.repository.CryllinkRepository import CryllinkRepository
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

class CrylletStatsService():

    @classmethod
    def getStats(cls):
        users = len(UserRepository.getAllUsers())
        cryllinks = CryllinkRepository.getAllCryllinks()
        payments = 0
        for cryllink in cryllinks:
            payments += cryllink.payments
        return {
            "users": users,
            "payments": payments,
            "cut_users": cls.getCutValue(users),
            "cut_payments": cls.getCutValue(payments)
        }

    @classmethod
    def getCutValue(cls, value):
        finalValue = str(value)[0]
        if(len(str(value))) <= 3:
            for i in range(len(str(value)[1:])):
                finalValue += "0"
        if(len(str(value))) == 4:
            finalValue += "K"
        if (len(str(value))) == 5:
            finalValue += "0K"
        if (len(str(value))) == 6:
            finalValue += "00K"
        if(len(str(value))) == 7:
            finalValue += "M"
        if(len(str(value))) == 8:
            finalValue += "0M"
        return finalValue


