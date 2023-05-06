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
            return {
                "created_cryllinks": len(cryllinks),
                "max_cryllinks": UserPermissions.getMaxCryllinksOf(userId),
                "cryllinks": Utils.createList(cryllinks)
            }

    @classmethod
    def get(cls, code):
        cryllink: Cryllink = CryllinkRepository.get(code)
        user: dict = UserService.getUserById(cryllink.user_id)
        return cryllink.toJson_Owner(user)

    @classmethod
    def remove(cls, cryllinkId):
        CryllinkRepository.remove(cryllinkId)
        return Utils.createSuccessResponse(True, Constants.CREATED)

    @classmethod
    def add(cls, request):
        cryllinks: list = CryllinkRepository.getCryllinksOf(request['user_id'])
        if not UserPermissions.canAdd(request['user_id'], len(cryllinks)):
            return Utils.createWrongResponse(False, Constants.MAX_CRYLLINKS_REACHED, 301), 301
        else:
            CryllinkRepository.add(request['user_id'], Utils.createCode(4), Constants.CRYPTO[request['crypto']], request['crypto'], request['description'], request['address'])
            return Utils.createSuccessResponse(True, Constants.CREATED)
