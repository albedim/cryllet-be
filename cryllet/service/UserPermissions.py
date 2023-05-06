from cryllet.model.entity.User import User
from cryllet.model.repository.UserRepository import UserRepository
from cryllet.utils.Constants import Constants
from cryllet.utils.Utils import Utils


class UserPermissions():

    __MAX_CRYLLINKS_PREMIUM = 50
    __MAX_CRYLLINKS_USER = 2

    @classmethod
    def getMaxCryllinksOf(cls, userId):
        user: User = UserRepository.getUserById(userId)
        if user is not None:
            return cls.__MAX_CRYLLINKS_PREMIUM if user.premium else cls.__MAX_CRYLLINKS_USER
        else:
            return 0

    @classmethod
    def canAdd(cls, userId, cryillinks):
        user: User = UserRepository.getUserById(userId)
        if user is not None:
            return True if cryillinks < cls.getMaxCryllinksOf(userId) else False
        else:
            return False