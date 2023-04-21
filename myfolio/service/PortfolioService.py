from myfolio.model.entity.Portfolio import Portfolio
from myfolio.model.entity.User import User
from myfolio.model.repository.PortfolioRepository import PortfolioRepository
from myfolio.model.repository.UserRepository import UserRepository
from myfolio.service.ExperienceService import ExperienceService
from myfolio.service.ProjectService import ProjectService
from myfolio.service.UserPermissionService import UserPermissionService
from myfolio.utils.Constants import Constants
from myfolio.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 19/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the portfolio service
#

class PortfolioService():

    @classmethod
    def add(cls, userId, request):
        if not UserPermissionService.canAddPortfolio(userId):
            return Utils.createWrongResponse(False, Constants.NOT_ENOUGH_PERMISSIONS, 306), 306
        else:
            PortfolioRepository.add(request['title'], request['description'], userId, request['skill'])
            return Utils.createSuccessResponse(True, Constants.CREATED)

    @classmethod
    def getPortfolios(cls, requestUserId, username):
        user: User = UserRepository.getUserByUsername(username)
        if user is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            portfolios: list[Portfolio] = PortfolioRepository.getPortfolios(user.user_id)
            return user.toJson_Portfolios_maxPortfolios_Editable(
                Utils.createList(portfolios),
                user.user_id == requestUserId,
                UserPermissionService.getMaxPortfolios(user.user_id)
            )

    @classmethod
    def getPortfolio(cls, requestUserId, portfolioId):
        portfolio: Portfolio = PortfolioRepository.getPortfolio(portfolioId)
        if portfolio is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            user: User = UserRepository.getUserById(portfolio.user_id)
            projects = ProjectService.getProjects(portfolioId)
            experiences = ExperienceService.get(portfolioId)
            return portfolio.toJson_Owner_Projects_Experiences_Editable_MaxProjects(
                user.toJson(),
                projects,
                experiences,
                portfolio.user_id == requestUserId,
                UserPermissionService.getMaxProjects(user.user_id)
            )
