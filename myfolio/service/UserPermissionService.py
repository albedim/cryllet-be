import base64
import datetime
import io
from datetime import timedelta
from flask_jwt_extended import create_access_token

from myfolio.model.entity.Portfolio import Portfolio
from myfolio.model.entity.User import User
from PIL import Image

from myfolio.model.repository.PortfolioRepository import PortfolioRepository
from myfolio.model.repository.UserRepository import UserRepository
from myfolio.service.LanguageService import LanguageService
from myfolio.service.SkillService import SkillService
from myfolio.utils.Constants import Constants
from myfolio.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 19/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user service
#

class UserPermissionService():

    @classmethod
    def canAdd(cls, userId):
        user: User = UserRepository.getUserById(userId)
        portfolios: int = len(PortfolioRepository.getPortfolios(userId))

        return (user.affiliate and portfolios < Constants.MAX_PORTFOLIOS_AFFILIATE) or \
               (user.premium and portfolios < Constants.MAX_PORTFOLIOS_PREMIUM) or \
               (not user.premium and not user.affiliate and portfolios < Constants.MAX_PORTFOLIOS)

    @classmethod
    def getMaxPortfolios(cls, userId):
        user: User = UserRepository.getUserById(userId)
        if user.affiliate:
            return Constants.MAX_PORTFOLIOS_AFFILIATE
        if user.premium:
            return Constants.MAX_PORTFOLIOS_PREMIUM
        return Constants.MAX_PORTFOLIOS
