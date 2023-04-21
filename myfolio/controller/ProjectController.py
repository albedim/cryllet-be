from flask import Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity

from myfolio.service.ProjectService import ProjectService
from myfolio.utils.Utils import Utils


project: Blueprint = Blueprint('ProjectController', __name__, url_prefix=Utils.getURL('project'))


@project.route("/get/<portfolioId>/<requestUserId>", methods=['GET'])
@cross_origin()
def get(portfolioId, requestUserId):
    return ProjectService.getProject(int(requestUserId), int(portfolioId))