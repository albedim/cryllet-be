from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin

from myfolio.service.LanguageService import LanguageService
from myfolio.service.SkillService import SkillService
from myfolio.service.UserService import UserService
from myfolio.utils.Utils import Utils


skill: Blueprint = Blueprint('SkillController', __name__, url_prefix=Utils.getURL('skill'))


@skill.route("/add", methods=['POST'])
@cross_origin()
def add():
    return SkillService.add(request.json)


@skill.route("/remove", methods=['DELETE'])
@cross_origin()
def remove():
    return SkillService.remove(request.args.get('user_id'), request.args.get('name'))
