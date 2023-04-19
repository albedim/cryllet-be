from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin

from myfolio.service.LanguageService import LanguageService
from myfolio.service.UserService import UserService
from myfolio.utils.Utils import Utils


language: Blueprint = Blueprint('LanguageController', __name__, url_prefix=Utils.getURL('language'))


@language.route("/add", methods=['POST'])
@cross_origin()
def add():
    return LanguageService.add(request.json)


@language.route("/remove", methods=['DELETE'])
@cross_origin()
def remove():
    return LanguageService.remove(request.args.get('user_id'), request.args.get('name'))
