from myfolio.configuration.config import sql
from myfolio.model.entity.Project import Project


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 21/04/23
# Created at: 19:35
# Version: 1.0.0
# Description: This is the class for the project repository
#

class ProjectRepository():

    @classmethod
    def add(cls, title, description, portfolioId):
        project: Project = Project(portfolioId, title, description)
        sql.session.add(project)
        sql.session.commit()

    @classmethod
    def getProjects(cls, portfolioId):
        projects: list[Project] = sql.session.query(Project).filter(Project.portfolio_id == portfolioId).all()
        return projects

    @classmethod
    def getProject(cls, projectId):
        project: Project = sql.session.query(Project).filter(Project.project_id == projectId).first()
        return project
