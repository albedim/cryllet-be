from flask import Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity

from myfolio.service.ExperienceService import ExperienceService
from myfolio.utils.Utils import Utils


experience: Blueprint = Blueprint('ExperienceController', __name__, url_prefix=Utils.getURL('experience'))

