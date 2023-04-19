import base64
import datetime
import io
from datetime import timedelta
from flask_jwt_extended import create_access_token

from myfolio.model.entity.Skill import Skill
from myfolio.model.entity.Skill import Skill
from myfolio.model.entity.User import User
from PIL import Image

from myfolio.model.repository.LanguageRepository import LanguageRepository
from myfolio.model.repository.SkillRepository import SkillRepository
from myfolio.model.repository.UserRepository import UserRepository
from myfolio.utils.Constants import Constants
from myfolio.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 18/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the skill service
#

class SkillService():

    @classmethod
    def add(cls, request):
        if cls.exists(request['name'], request['user_id']):
            return Utils.createWrongResponse(False, Constants.ALREADY_CREATED, 409), 409
        else:
            SkillRepository.add(request['name'], request['user_id'])
            return Utils.createSuccessResponse(True, Constants.CREATED)

    @classmethod
    def getSkills(cls, userId):
        skills: list[Skill] = SkillRepository.getSkills(userId)
        return Utils.createList(skills)

    @classmethod
    def exists(cls, name, userId):
        return SkillRepository.exists(name, userId) is not None

    @classmethod
    def remove(cls, userId, name):
        SkillRepository.remove(userId, name)
        return Utils.createSuccessResponse(True, Constants.CREATED)
