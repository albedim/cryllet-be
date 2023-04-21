from myfolio.configuration.config import sql
from myfolio.model.entity.Experience import Experience


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 21/04/23
# Created at: 19:35
# Version: 1.0.0
# Description: This is the class for the experience repository
#

class ExperienceRepository():

    @classmethod
    def add(cls, title, startDate, endDate, roles, portfolioId):
        experience: Experience = Experience(portfolioId, title, startDate, endDate, roles)
        sql.session.add(experience)
        sql.session.commit()

    @classmethod
    def getExperiences(cls, portfolioId):
        experiences: list[Experience] = sql.session.query(Experience).filter(Experience.portfolio_id == portfolioId).all()
        return experiences
