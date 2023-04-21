from myfolio.model.repository.LikeRepository import LikeRepository
from myfolio.utils.Constants import Constants
from myfolio.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 21/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the like service
#

class LikeService():

    @classmethod
    def add(cls, request):
        # user id is null, not logged in
        if request['user_id'] is None:
            return Utils.createWrongResponse(False, Constants.NOT_ENOUGH_PERMISSIONS, 306), 306
        else:
            like = LikeRepository.get(request['user_id'], request['project_id'])
            # like doesn't exist, create it
            if like is None:
                LikeRepository.add(request['user_id'], request['project_id'], request['liked'])
            else:
                # like exists, check if it's not the same as before
                if like.liked != request['liked']:
                    LikeRepository.changeType(like)
            return Utils.createSuccessResponse(True, Constants.CREATED)
