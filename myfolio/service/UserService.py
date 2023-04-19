import base64
import datetime
import io
from datetime import timedelta
from flask_jwt_extended import create_access_token
from myfolio.model.entity.User import User
from PIL import Image
from myfolio.model.repository.UserRepository import UserRepository
from myfolio.service.LanguageService import LanguageService
from myfolio.service.SkillService import SkillService
from myfolio.utils.Constants import Constants
from myfolio.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 18/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user service
#

class UserService():

    @classmethod
    def signin(cls, request: dict):
        try:
            user: User = UserRepository.signin(
                request['email'],
                request['password']
            )
            if user is not None:
                # need to split user token and image because the image is too large to be inside the token
                return Utils.createSuccessResponse(True, {
                    "token": create_access_token(
                        identity=user.toJson(),
                        expires_delta=timedelta(weeks=4)),
                    "image": cls.encodeImage(user.image)
                })
            else:
                return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def existsByEmail(cls, email) -> bool:
        return UserRepository.getUserByEmail(email) is not None

    @classmethod
    def existsByUsername(cls, username) -> bool:
        return UserRepository.getUserByUsername(username) is not None

    @classmethod
    def getUserById(cls, userId):
        try:
            user: User = UserRepository.getUserById(userId)
            return user.toJson_Image(cls.encodeImage(user.image))
        except AttributeError:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404

    @classmethod
    def getUserByUsername(cls, username):
        try:
            user: User = UserRepository.getUserByUsername(username)
            languages: list[dict] = LanguageService.getLanguages(user.user_id)
            skills: list[dict] = SkillService.getSkills(user.user_id)
            return user.toJson_Image_Skills_Languages(cls.encodeImage(user.image), skills, languages)
        except AttributeError:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404

    @classmethod
    def signup(cls, request: dict):
        try:
            if cls.existsByEmail(request['email'] or cls.existsByUsername(request['username'])):
                return Utils.createWrongResponse(False, Constants.ALREADY_CREATED, 409), 409
            else:
                imageName = f"myfolio/files/profileImages/{str(datetime.datetime.now()).replace('-', '').replace('.', '').replace(' ', '').replace(':', '')}.png"
                UserRepository.signup(
                    request['birthday'],
                    request['first_name'],
                    request['last_name'],
                    request['email'],
                    request['username'],
                    request['password'],
                    request['introduction'],
                    Constants.DEFAULT_IMAGE if request['image'] is None else imageName
                )
                if request['image'] is not None:
                    cls.decodeImage(request['image'], imageName)
                return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def createForgottenPasswordToken(cls, email):
        user: User = UserRepository.getUserByEmail(email)
        if user is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            token: str = Utils.createLink(140)
            UserRepository.createForgottenPasswordToken(user, token)
            Utils.sendPasswordForgottenEmail(user.email, token)
            return Utils.createSuccessResponse(True, Constants.CREATED), 200

    @classmethod
    def getUserByPasswordForgottenToken(cls, token):
        user: User = UserRepository.getUserByPasswordForgottenToken(token)
        if user is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            return Utils.createSuccessResponse(True, user.user_id), 200

    @classmethod
    def changePassword(cls, request):
        try:
            UserRepository.changePassword(request['user_id'], request['new_password'])
            return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def changeIntroduction(cls, userId, request):
        try:
            UserRepository.changeIntroduction(userId, request['new_introduction'])
            return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def decodeImage(cls, image, imageName):
        decodedImage = base64.b64decode(str(image))
        file = Image.open(io.BytesIO(decodedImage))
        file.save(imageName, 'png')

    @classmethod
    def encodeImage(cls, imageName):
        with open(imageName, "rb") as image:
            encodedImage = base64.b64encode(image.read())
        return str(encodedImage)

    @classmethod
    def sync(cls, requestUser):
        user: User = UserRepository.getUserById(requestUser['user_id'])
        userJson: dict = user.toJson_Role(RoleService.getRole(user.role_id))
        if userJson == requestUser:
            return Utils.createSuccessResponse(True, Constants.UP_TO_DATE)
        else:
            return Utils.createWrongResponse(False, {
                "token": create_access_token(
                    identity=user.toJson(),
                    expires_delta=timedelta(weeks=4)),
                "image": cls.encodeImage(user.image)
            }, 306), 306

