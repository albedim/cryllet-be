import datetime

from cryllet.configuration.config import sql
from cryllet.utils.Constants import Constants


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/05/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the cryllink entity
#


class Cryllink(sql.Model):
    __tablename__ = 'cryllinks'
    cryllink_id: int = sql.Column(sql.Integer, primary_key=True)
    views: int = sql.Column(sql.Integer, nullable=False)
    money: int = sql.Column(sql.Integer, nullable=False)
    payments: int = sql.Column(sql.Integer, nullable=False)
    user_id: int = sql.Column(sql.Integer, nullable=False)
    code: str = sql.Column(sql.String(54), nullable=False)
    crypto: str = sql.Column(sql.String(3), nullable=False)
    crypto_name: str = sql.Column(sql.String(14), nullable=False)
    description: str = sql.Column(sql.String(140), nullable=False)
    address: str = sql.Column(sql.String(1024), nullable=False)

    def __init__(self, user_id, code, crypto_name, crypto, description, address):
        self.user_id = user_id
        self.views = 0
        self.payments = 0
        self.money = 0
        self.code = code
        self.crypto = crypto
        self.crypto_name = crypto_name
        self.address = address
        self.description = description

    def toJson(self):
        return {
            'cryllink_id': self.cryllink_id,
            'views': self.views,
            'payments': self.payments,
            'money': self.money,
            'user_id': self.user_id,
            'code': self.code,
            'crypto_name': self.crypto_name,
            'crypto': self.crypto,
            'address': self.address,
            'description': self.description
        }

    def toJson_Locked(self, locked):
        return {
            'cryllink_id': self.cryllink_id,
            'locked': locked,
            'views': self.views,
            'payments': self.payments,
            'money': self.money,
            'user_id': self.user_id,
            'code': self.code,
            'crypto_name': self.crypto_name,
            'crypto': self.crypto,
            'address': self.address,
            'description': self.description
        }

    def toJson_Owner(self, user):
        return {
            'cryllink_id': self.cryllink_id,
            'owner': user,
            'views': self.views,
            'payments': self.payments,
            'money': self.money,
            'user_id': self.user_id,
            'code': self.code,
            'crypto_name': self.crypto_name,
            'crypto': self.crypto,
            'address': self.address,
            'description': self.description
        }

    def toJson_Owner_Locked(self, user, locked):
        return {
            'cryllink_id': self.cryllink_id,
            'locked': locked,
            'owner': user,
            'views': self.views,
            'payments': self.payments,
            'money': self.money,
            'user_id': self.user_id,
            'code': self.code,
            'crypto_name': self.crypto_name,
            'crypto': self.crypto,
            'address': self.address,
            'description': self.description
        }