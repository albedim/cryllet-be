import datetime

from myfolio.configuration.config import sql
from myfolio.utils.Constants import Constants


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 21/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the experience entity
#


class Experience(sql.Model):
    __tablename__ = 'experiences'
    experience_id: int = sql.Column(sql.Integer, primary_key=True)
    portfolio_id: int = sql.Column(sql.Integer, nullable=False)
    title: str = sql.Column(sql.String(54), nullable=False)
    start_date: datetime.date = sql.Column(sql.Date, nullable=False)
    end_date: datetime.date = sql.Column(sql.Date, nullable=True)
    roles: str = sql.Column(sql.String(240), nullable=False)

    def __init__(self, portfolioId, title, startDate, endDate, roles):
        self.title = title
        self.portfolio_id = portfolioId
        self.start_date = startDate
        self.end_date = endDate
        self.roles = roles

    def toJson(self):
        return {
            'experience_id': self.experience_id,
            'portfolio_id': self.portfolio_id,
            'title': self.title,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date) if self.end_date is not None else None,
            'roles': self.roles.split(',')
        }