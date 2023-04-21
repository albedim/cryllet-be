import datetime

from myfolio.configuration.config import sql
from myfolio.utils.Constants import Constants


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 21/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the like entity
#


class Like(sql.Model):
    __tablename__ = 'likes'
    like_id: int = sql.Column(sql.Integer, primary_key=True)
    user_id: int = sql.Column(sql.Integer, nullable=False)
    project_id: int = sql.Column(sql.Integer, nullable=False)
    liked: bool = sql.Column(sql.Integer, nullable=False)
    unliked: bool = sql.Column(sql.Integer, nullable=False)

    def __init__(self, projectId, userId, liked, unliked):
        self.project_id = projectId
        self.user_id = userId
        self.unliked = unliked
        self.liked = liked

    def toJson(self):
        return {
            'like_id': self.like_id,
            'project_id': self.project_id,
            'user_id': self.user_id,
            'unliked': self.unliked,
            'liked': self.liked
        }