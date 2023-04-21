import datetime

from myfolio.configuration.config import sql
from myfolio.utils.Constants import Constants


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 18/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user entity
#


class User(sql.Model):
    __tablename__ = 'users'
    user_id: int = sql.Column(sql.Integer, primary_key=True)
    first_name: str = sql.Column(sql.String(20), nullable=False)
    last_name: str = sql.Column(sql.String(20), nullable=False)
    email: str = sql.Column(sql.String(40), nullable=False)
    password: str = sql.Column(sql.String(40), nullable=False)
    birthday: str = sql.Column(sql.String(10), nullable=False)
    username: str = sql.Column(sql.String(40), nullable=False)
    introduction: str = sql.Column(sql.String(240), nullable=False)
    password_forgotten_token: str = sql.Column(sql.String(540), nullable=True)
    image: str = sql.Column(sql.String(140), nullable=True)
    affiliate: bool = sql.Column(sql.Boolean, nullable=False)
    premium: bool = sql.Column(sql.Boolean, nullable=False)
    created_on: datetime.date = sql.Column(sql.Date, nullable=False)

    def __init__(self, first_name, last_name, email, username, password, introduction, birthday, image):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.birthday = birthday
        self.username = username
        self.introduction = introduction
        self.password_forgotten_token = None
        self.image = image
        self.affiliate = False
        self.premium = False
        self.created_on = datetime.date.today()

    def toJson(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'username': self.username,
            'birthday': self.birthday,
            'introduction': self.introduction,
            'affiliate': self.affiliate,
            'premium': self.premium,
            'created_on': str(self.created_on)
        }

    def toJson_Image_Skills_Languages_Editable(self, image, skills, languages, editable):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'username': self.username,
            'birthday': self.birthday,
            'introduction': self.introduction,
            'image': image,
            'premium': self.premium,
            'affiliate': self.affiliate,
            'skills': skills,
            'languages': languages,
            'editable': editable,
            'created_on': str(self.created_on)
        }

    def toJson_Portfolios_maxPortfolios_Editable(self, portfolios, editable, maxPortfolios):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'username': self.username,
            'birthday': self.birthday,
            'introduction': self.introduction,
            'premium': self.premium,
            'affiliate': self.affiliate,
            'portfolios_section': {
                'portfolios': portfolios,
                'editable': editable,
                'addable': len(portfolios) < maxPortfolios,
                'created_portfolios': len(portfolios),
                'max_portfolios': maxPortfolios,
            },
            'created_on': str(self.created_on)
        }
