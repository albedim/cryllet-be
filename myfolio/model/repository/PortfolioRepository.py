from sqlalchemy import text
from myfolio.configuration.config import sql
from myfolio.model.entity.Portfolio import Portfolio


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 19/04/23
# Created at: 19:35
# Version: 1.0.0
# Description: This is the class for the language repository
#

class PortfolioRepository():

    @classmethod
    def add(cls, title, description, userId, skill):
        portfolio: Portfolio = Portfolio(title, userId, description, skill)
        sql.session.add(portfolio)
        sql.session.commit()

    @classmethod
    def getPortfolios(cls, userId):
        portfolios: list[Portfolio] = sql.session.query(Portfolio).filter(Portfolio.user_id == userId).all()
        return portfolios

    @classmethod
    def getPortfolioByProject(cls, projectId):
        portfolio: list[Portfolio] = sql.session.query(Portfolio).from_statement(
            text('SELECT portfolios.* '
                 'FROM portfolios '
                 'JOIN projects '
                 'ON portfolios.portfolio_id = projects.portfolio_id '
                 'AND projects.project_id = :projectId').params(projectId=projectId)
        ).first()
        return portfolio

    @classmethod
    def getPortfolio(cls, portfolioId):
        portfolio: Portfolio = sql.session.query(Portfolio).filter(Portfolio.portfolio_id == portfolioId).first()
        return portfolio
