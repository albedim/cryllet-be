import base64
import datetime
import io
from datetime import timedelta
from typing import Any, Tuple

from flask_jwt_extended import create_access_token

from cryllet.model.entity.Cryllink import Cryllink
from cryllet.model.entity.User import User
from cryllet.model.repository.CryllinkRepository import CryllinkRepository
from cryllet.model.repository.UserRepository import UserRepository
from cryllet.service.UserPermissions import UserPermissions
from cryllet.service.UserService import UserService
from cryllet.utils.Constants import Constants
from cryllet.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/05/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the cryllink service
#

class CryllinkService():

    @classmethod
    def getCryllinksOf(cls, userId):
        user: User = UserRepository.getUserById(userId)
        if user is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            cryllinks: list = CryllinkRepository.getCryllinksOf(userId)
            result = []
            for cryllink in cryllinks:
                if UserPermissions.canAddPayment(cryllink.cryllink_id):
                    result.append(cryllink.toJson_Locked(False))
                else:
                    result.append(cryllink.toJson_Locked(True))
            return {
                "max_payments": UserPermissions.getMaxPayments(user.user_id),
                "max_cryllinks": 5,
                "cryllinks": result
            }

    @classmethod
    def existsByAddress(cls, address):
        return CryllinkRepository.getByAddress(address) is not None

    @classmethod
    def get(cls, code):
        cryllink: Cryllink = CryllinkRepository.getByCode(code)
        user: dict = UserService.getUserById(cryllink.user_id)
        return cryllink.toJson_Owner_Locked(user, cryllink.payments >= UserPermissions.getMaxPayments(cryllink.user_id))

    @classmethod
    def remove(cls, cryllinkId):
        CryllinkRepository.remove(cryllinkId)
        return Utils.createSuccessResponse(True, Constants.CREATED)

    @classmethod
    def add(cls, request):
        if cls.existsByAddress(request['address']):
            return Utils.createWrongResponse(False, Constants.CRYLLINK_ALREADY_CREATED, 409), 409
        else:
            cryllinks: list = CryllinkRepository.getCryllinksOf(request['user_id'])
            if len(cryllinks) < 5:
                CryllinkRepository.add(request['user_id'], Utils.createCode(10), Constants.CRYPTO[request['crypto']], request['crypto'], request['description'], request['address'])
                return Utils.createSuccessResponse(True, Constants.CREATED)
            else:
                return Utils.createWrongResponse(False, Constants.MAX_CRYLLINKS_REACHED, 301), 301

    @classmethod
    def addView(cls, cryllinkId):
        CryllinkRepository.addView(cryllinkId)
        return Utils.createSuccessResponse(True, Constants.CREATED)

    @classmethod
    def addPayment(cls, request):
        if UserPermissions.canAddPayment(request['cryllink_id']):
            CryllinkRepository.addPayment(request['cryllink_id'])
            CryllinkRepository.addMoney(request['cryllink_id'], int(request['money']))
            return Utils.createSuccessResponse(True, Constants.CREATED)
        else:
            return Utils.createWrongResponse(False, Constants.MAX_CRYLLINKS_REACHED, 301), 301
