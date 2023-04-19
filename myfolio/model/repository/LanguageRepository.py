from myfolio.configuration.config import sql
from myfolio.model.entity.Language import Language
from myfolio.model.entity.User import User


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 18/04/23
# Created at: 19:35
# Version: 1.0.0
# Description: This is the class for the language repository
#

class LanguageRepository():

    @classmethod
    def add(cls, name, level, userId):
        language: Language = Language(name, level, userId)
        sql.session.add(language)
        sql.session.commit()

    @classmethod
    def exists(cls, name, userId):
        language: Language = sql.session.query(Language).filter(Language.name == name).filter(Language.user_id == userId).first()
        return language

    @classmethod
    def getLanguages(cls, userId):
        languages: list[Language] = sql.session.query(Language).filter(Language.user_id == userId).all()
        return languages

    @classmethod
    def remove(cls, userId, name):
        language: Language = sql.session.query(Language).filter(Language.user_id == userId).filter(Language.name == name).delete()
        sql.session.commit()
