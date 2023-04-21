import datetime

from myfolio.configuration.config import sql
from myfolio.utils.Constants import Constants


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 21/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the project entity
#


class Project(sql.Model):
    __tablename__ = 'projects'
    project_id: int = sql.Column(sql.Integer, primary_key=True)
    user_id: int = sql.Column(sql.Integer, nullable=False)
    created_on: datetime.date = sql.Column(sql.Date, nullable=False)
    portfolio_id: int = sql.Column(sql.Integer, nullable=False)
    title: str = sql.Column(sql.String(54), nullable=False)
    description: str = sql.Column(sql.String(240), nullable=False)

    def __init__(self, portfolioId, userId, createOn, title, description):
        self.title = title
        self.user_id = userId
        self.created_on = createOn
        self.portfolio_id = portfolioId
        self.description = description

    def toJson(self):
        return {
            'project_id': self.project_id,
            'portfolio_id': self.portfolio_id,
            'user_id': self.user_id,
            'title': self.title,
            'created_on': str(self.created_on),
            'description': self.description,
        }

    def toJson_Editable_Liked(self, editable, like):
        return {
            'project_id': self.project_id,
            'portfolio_id': self.portfolio_id,
            'user_id': self.user_id,
            'title': self.title,
            'editable': editable,
            'created_on': str(self.created_on),
            'description': self.description,
            'like': like
        }