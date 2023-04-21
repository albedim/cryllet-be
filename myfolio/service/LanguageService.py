from myfolio.model.entity.Language import Language
from myfolio.model.repository.LanguageRepository import LanguageRepository
from myfolio.utils.Constants import Constants
from myfolio.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 18/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the language service
#

class LanguageService():

    @classmethod
    def add(cls, request):
        if cls.exists(request['name'], request['user_id']):
            return Utils.createWrongResponse(False, Constants.ALREADY_CREATED, 409), 409
        else:
            LanguageRepository.add(request['name'], request['level'], request['user_id'])
            return Utils.createSuccessResponse(True, Constants.CREATED)

    @classmethod
    def getLanguages(cls, userId):
        languages: list[Language] = LanguageRepository.getLanguages(userId)
        return Utils.createList(languages)

    @classmethod
    def exists(cls, name, userId):
        return LanguageRepository.exists(name, userId) is not None

    @classmethod
    def remove(cls, userId, name):
        LanguageRepository.remove(userId, name)
        return Utils.createSuccessResponse(True, Constants.CREATED)
