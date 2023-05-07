from cryllet.configuration.config import sql
from cryllet.model.entity.Cryllink import Cryllink
from cryllet.model.entity.User import User


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/05/23
# Created at: 19:35
# Version: 1.0.0
# Description: This is the class for the cryllink repository
#

class CryllinkRepository():

    @classmethod
    def add(cls, user_id, code, crypto_name, crypto, description, address):
        cryllink: Cryllink = Cryllink(user_id, code, crypto_name, crypto, description, address)
        sql.session.add(cryllink)
        sql.session.commit()

    @classmethod
    def getByCode(cls, code):
        cryllink: Cryllink = sql.session.query(Cryllink).filter(Cryllink.code == code).first()
        return cryllink

    @classmethod
    def getById(cls, cryllinkId):
        cryllink: Cryllink = sql.session.query(Cryllink).filter(Cryllink.cryllink_id == cryllinkId).first()
        return cryllink

    @classmethod
    def getCryllinksOf(cls, userId):
        cryllinks: list = sql.session.query(Cryllink).filter(Cryllink.user_id == userId).all()
        return cryllinks

    @classmethod
    def addView(cls, cryllinkId):
        cryllink: Cryllink = cls.getById(cryllinkId)
        cryllink.views += 1
        sql.session.commit()

    @classmethod
    def remove(cls, cryllinkId):
        cryllink: Cryllink = sql.session.query(Cryllink).filter(Cryllink.cryllink_id == cryllinkId).delete()
        sql.session.commit()
