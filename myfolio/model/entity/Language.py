import datetime

from myfolio.configuration.config import sql
from myfolio.utils.Constants import Constants


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 18/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the language entity
#


class Language(sql.Model):
    __tablename__ = 'languages'
    language_id: int = sql.Column(sql.Integer, primary_key=True)
    name: str = sql.Column(sql.String(20), nullable=False)
    level: str = sql.Column(sql.String(14), nullable=False)
    user_id: int = sql.Column(sql.Integer, nullable=False)

    def __init__(self, name, level, userId):
        self.name = name
        self.level = level
        self.user_id = userId

    def toJson(self):
        return {
            'language_id': self.language_id,
            'name': self.name,
            'level': self.level,
            'user_id': self.user_id
        }