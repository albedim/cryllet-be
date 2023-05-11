from cryllet.model.entity.Cryllink import Cryllink
from cryllet.model.entity.User import User
from cryllet.model.repository.CryllinkRepository import CryllinkRepository
from cryllet.model.repository.UserRepository import UserRepository
from cryllet.utils.Constants import Constants
from cryllet.utils.Utils import Utils


class UserPermissions():

    __MAX_PAYMENTS_PREMIUM = 250
    __MAX_PAYMENTS_USER = 250

    @classmethod
    def canAddPayment(cls, cryllinkId):
        cryllink: Cryllink = CryllinkRepository.getById(cryllinkId)
        if cryllink is not None:
            return cryllink.payments < cls.getMaxPayments(cryllink.user_id)
        else:
            return False

    @classmethod
    def getMaxPayments(cls, userId):
        user: User = UserRepository.getUserById(userId)
        return cls.__MAX_PAYMENTS_PREMIUM if user.premium else cls.__MAX_PAYMENTS_USER