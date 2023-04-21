from myfolio.model.repository.ExperienceRepository import ExperienceRepository
from myfolio.utils.Constants import Constants
from myfolio.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 21/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the experience service
#

class ExperienceService():

    @classmethod
    def add(cls, request):
        ExperienceRepository.add(
            request['title'],
            request['start_date'],
            request['end_date'],
            request['roles'],
            request['portfolio_id']
        )
        return Utils.createSuccessResponse(True, Constants.CREATED)

    @classmethod
    def get(cls, portfolioId):
        experiences = ExperienceRepository.getExperiences(portfolioId)
        result = []
        for experience in experiences:
            result.append(experience.toJson())
        return result
