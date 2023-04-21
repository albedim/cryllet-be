from myfolio.configuration.config import sql


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 18/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the skill entity
#


class Skill(sql.Model):
    __tablename__ = 'skills'
    skill_id: int = sql.Column(sql.Integer, primary_key=True)
    name: str = sql.Column(sql.String(20), nullable=False)
    user_id: int = sql.Column(sql.Integer, nullable=False)

    def __init__(self, name, userId):
        self.name = name
        self.user_id = userId

    def toJson(self):
        return {
            'language_id': self.skill_id,
            'name': self.name,
            'user_id': self.user_id
        }