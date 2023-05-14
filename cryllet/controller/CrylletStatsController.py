from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin

from cryllet.service.CrylletStatsService import CrylletStatsService
from cryllet.service.CryllinkService import CryllinkService
from cryllet.service.UserService import UserService
from cryllet.utils.Utils import Utils


crylletStats: Blueprint = Blueprint('CrylletStatsController', __name__, url_prefix=Utils.getURL('crylletStats'))


@crylletStats.route("/get", methods=['GET'])
@cross_origin()
def signin():
    return CrylletStatsService.getStats()



