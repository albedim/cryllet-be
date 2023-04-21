from myfolio.configuration.config import sql
from myfolio.model.entity.Skill import Skill


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 18/04/23
# Created at: 19:35
# Version: 1.0.0
# Description: This is the class for the skill repository
#

class SkillRepository():

    @classmethod
    def add(cls, name, userId):
        skill: Skill = Skill(name, userId)
        sql.session.add(skill)
        sql.session.commit()

    @classmethod
    def exists(cls, name, userId):
        skill: Skill = sql.session.query(Skill).filter(Skill.name == name).filter(Skill.user_id == userId).first()
        return skill

    @classmethod
    def getSkills(cls, userId):
        skills: list[Skill] = sql.session.query(Skill).filter(Skill.user_id == userId).all()
        return skills

    @classmethod
    def remove(cls, userId, name):
        skill: Skill = sql.session.query(Skill).filter(Skill.user_id == userId).filter(Skill.name == name).delete()
        sql.session.commit()
