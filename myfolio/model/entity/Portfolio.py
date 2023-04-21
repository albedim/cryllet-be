import datetime

from myfolio.configuration.config import sql
from myfolio.utils.Constants import Constants


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 19/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the portfolio entity
#


class Portfolio(sql.Model):
    __tablename__ = 'portfolios'
    portfolio_id: int = sql.Column(sql.Integer, primary_key=True)
    user_id: int = sql.Column(sql.Integer, nullable=False)
    skill: str = sql.Column(sql.String(20), nullable=False)
    title: str = sql.Column(sql.String(54), nullable=False)
    created_on: datetime.date = sql.Column(sql.Date, nullable=False)
    description: str = sql.Column(sql.String(240), nullable=False)

    def __init__(self, title, userId, description, skill):
        self.user_id = userId
        self.skill = skill
        self.title = title
        self.description = description
        self.created_on = datetime.date.today()

    def toJson(self):
        return {
            'portfolio_id': self.portfolio_id,
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
            'skill': self.skill,
            'created_on': str(self.created_on)
        }

    def toJson_Owner_Projects_Experiences_Editable_MaxProjects(self, owner, projects, experiences, editable, maxProjects):
        return {
            'portfolio_id': self.portfolio_id,
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
            'skill': self.skill,
            'owner': owner,
            'projects_section': {
                'projects': projects,
                'max_projects': maxProjects,
                'created_projects': len(projects),
                'addable': len(projects) < maxProjects
            },
            'experiences': experiences,
            'editable': editable,
            'created_on': str(self.created_on)
        }