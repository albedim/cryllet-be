from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin

from cryllet.service.CryllinkService import CryllinkService
from cryllet.service.UserService import UserService
from cryllet.utils.Utils import Utils


cryllink: Blueprint = Blueprint('CryllinkController', __name__, url_prefix=Utils.getURL('cryllink'))


@cryllink.route("/get/of/<userId>", methods=['GET'])
@cross_origin()
def signin(userId):
    return CryllinkService.getCryllinksOf(userId)


@cryllink.route("/get/<code>", methods=['GET'])
@cross_origin()
def get(code):
    return CryllinkService.get(code)


@cryllink.route("/add", methods=['POST'])
@cross_origin()
def create():
    return CryllinkService.add(request.json)


@cryllink.route("/add_view/<cryllinkId>", methods=['PUT'])
@cross_origin()
def addView(cryllinkId):
    return CryllinkService.addView(cryllinkId)


@cryllink.route("/add_payment/", methods=['PUT'])
@cross_origin()
def addPayment():
    return CryllinkService.addPayment(request.json)


@cryllink.route("/remove/<cryllinkId>", methods=['DELETE'])
@cross_origin()
def remove(cryllinkId):
    return CryllinkService.remove(cryllinkId)


