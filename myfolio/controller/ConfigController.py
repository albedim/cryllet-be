from flask import Blueprint
from flask_cors import cross_origin

from myfolio.service.ConfigService import ConfigService
from myfolio.utils.Utils import Utils


config: Blueprint = Blueprint('ConfigController', __name__, url_prefix=Utils.getURL('config'))


@config.route("/get/languages", methods=['GET'])
@cross_origin()
def getLanguages():
    return ConfigService.getLanguages()