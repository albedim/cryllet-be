from myfolio.configuration.config import sql
from myfolio.model.entity.Like import Like


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 21/04/23
# Created at: 19:35
# Version: 1.0.0
# Description: This is the class for the like repository
#

class LikeRepository():

    @classmethod
    def add(cls, userId, projectId, liked):
        like: Like = Like(projectId, userId, liked, not liked)
        sql.session.add(like)
        sql.session.commit()

    @classmethod
    def get(cls, userId, projectId):
        like: Like = sql.session.query(Like).filter(Like.user_id == userId).filter(Like.project_id == projectId).first()
        return like

    @classmethod
    def getLikes(cls, projectId):
        likes: list[Like] = sql.session.query(Like).filter(Like.project_id == projectId).filter(Like.liked).all()
        return likes

    @classmethod
    def getUnlikes(cls, projectId):
        likes: list[Like] = sql.session.query(Like).filter(Like.project_id == projectId).filter(Like.unliked).all()
        return likes

    @classmethod
    def changeType(cls, like):
        like: Like = sql.session.query(Like).filter(Like.like_id == like.like_id).first()
        like.liked = not like.liked
        like.unliked = not like.unliked
        sql.session.commit()
