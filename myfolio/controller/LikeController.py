from flask import Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity

from myfolio.service.LikeService import LikeService
from myfolio.service.ProjectService import ProjectService
from myfolio.utils.Utils import Utils


like: Blueprint = Blueprint('LikeController', __name__, url_prefix=Utils.getURL('like'))


@like.route("/add", methods=['POST'])
@cross_origin()
def get():
    return LikeService.add(request.json)