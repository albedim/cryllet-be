from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from myfolio.service.UserService import UserService
from myfolio.utils.Utils import Utils


user: Blueprint = Blueprint('UserController', __name__, url_prefix=Utils.getURL('user'))


@user.route("/signin", methods=['POST'])
@cross_origin()
def signin():
    return UserService.signin(request.json)


@user.route("/sync", methods=['GET'])
@cross_origin()
@jwt_required()
def isExpired():
    return UserService.sync(get_jwt_identity())


@user.route("/password_forgotten_token/<email>", methods=['PUT'])
@cross_origin()
def createPasswordForgottenToken(email):
    return UserService.createForgottenPasswordToken(email)


@user.route("/change/introduction", methods=['PUT'])
@jwt_required()
@cross_origin()
def changeIntroduction():
    return UserService.changeIntroduction(get_jwt_identity()['user_id'], request.json)


@user.route("/password_forgotten_token/<token>", methods=['GET'])
@cross_origin()
def getUserByPasswordForgottenToken(token):
    return UserService.getUserByPasswordForgottenToken(token)


@user.route("/change_password", methods=['PUT'])
@cross_origin()
def changePassword():
    return UserService.changePassword(request.json)


@user.route("/get/id/<userId>", methods=['GET'])
@cross_origin()
def getById(userId):
    return UserService.getUserById(userId)


@user.route("/get/username/<username>", methods=['GET'])
@cross_origin()
def getByUsername(username):
    return UserService.getUserByUsername(username)


@user.route("/signup", methods=['POST'])
@cross_origin()
def signup():
    return UserService.signup(request.json)
