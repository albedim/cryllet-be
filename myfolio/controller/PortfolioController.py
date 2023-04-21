from flask import Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity

from myfolio.service.PortfolioService import PortfolioRepository, PortfolioService
from myfolio.utils.Utils import Utils


portfolio: Blueprint = Blueprint('PortfolioController', __name__, url_prefix=Utils.getURL('portfolio'))


@portfolio.route("/get/of/<username>/<requestUserId>", methods=['GET'])
@cross_origin()
def getPortfolios(username, requestUserId):
    return PortfolioService.getPortfolios(int(requestUserId), username)


@portfolio.route("/get/<portfolioId>/<requestUserId>", methods=['GET'])
@cross_origin()
def getPortfolio(portfolioId, requestUserId):
    return PortfolioService.getPortfolio(int(requestUserId), int(portfolioId))
