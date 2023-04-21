from myfolio.model.entity.User import User
from myfolio.model.repository.PortfolioRepository import PortfolioRepository
from myfolio.model.repository.ProjectRepository import ProjectRepository
from myfolio.model.repository.UserRepository import UserRepository
from myfolio.utils.Constants import Constants


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 19/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user service
#

class UserPermissionService():

    @classmethod
    def canAddPortfolio(cls, userId):
        user: User = UserRepository.getUserById(userId)
        portfolios: int = len(PortfolioRepository.getPortfolios(userId))

        return (user.affiliate and portfolios < Constants.MAX_PORTFOLIOS_AFFILIATE) or \
               (user.premium and portfolios < Constants.MAX_PORTFOLIOS_PREMIUM) or \
               (not user.premium and not user.affiliate and portfolios < Constants.MAX_PORTFOLIOS)

    @classmethod
    def canAddProjectToPortfolio(cls, userId, portfolioId):
        user: User = UserRepository.getUserById(userId)
        portfolio = PortfolioRepository.getPortfolio(portfolioId)
        projects: int = len(ProjectRepository.getProjects(portfolioId))

        return (portfolio.user_id == userId) and \
               (user.affiliate and projects < Constants.MAX_PROJECTS_AFFILIATE) or \
               (user.premium and projects < Constants.MAX_PROJECTS_PREMIUM) or \
               (not user.premium and not user.affiliate and projects < Constants.MAX_PROJECTS)

    @classmethod
    def getMaxPortfolios(cls, userId):
        user: User = UserRepository.getUserById(userId)
        if user.affiliate:
            return Constants.MAX_PORTFOLIOS_AFFILIATE
        if user.premium:
            return Constants.MAX_PORTFOLIOS_PREMIUM
        return Constants.MAX_PORTFOLIOS

    @classmethod
    def getMaxProjects(cls, userId):
        user: User = UserRepository.getUserById(userId)
        if user.affiliate:
            return Constants.MAX_PROJECTS_AFFILIATE
        if user.premium:
            return Constants.MAX_PROJECTS_PREMIUM
        return Constants.MAX_PROJECTS
