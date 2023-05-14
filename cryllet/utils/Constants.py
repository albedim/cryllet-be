
#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 18/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the constants
#

class Constants():

    USER_NOT_FOUND: str = "This user was not found. If you forgot your password recover your account"
    NOT_FOUND: str = "Not found"
    MAX_CRYLLINKS_REACHED: str = "You can't add more cryllinks"
    NOT_ENOUGH_PERMISSIONS: str = "Not enough permissions"
    CREATED: str = "Created"
    UP_TO_DATE: str = "Up To date"
    NOT_UP_TO_DATE: str = "Not Up To date"
    ALREADY_CREATED = "This resource was already created"
    CRYLLINK_ALREADY_CREATED = "A cryllink with this address already exists"
    INVALID_REQUEST: str = "Invalid request"

    CRYPTO = {
        # 'btc': 'Bitcoin',
        'eth': 'Ethereum'
    }

    PROMO_CODES = [
        # 'PREMIUMFREE'
    ]

    EMAIL = 'crylletinc@gmail.com'
    PASSWORD = 'hlvvqpdubniuobbe'
    PASSWORD_FORGOTTEN_EMAIL: str = "Hey! \nHere's the link to recover your account: https://cryllet-fe.pages.dev/create_password/{token}"

    PAGE_NOT_FOUND = 'This page was not found. See our documentation'
    PAGE_METHOD_NOT_ALLOWED = 'Method not allowed. See our documentation'
    PAGE_UNKNOWN_ERROR = 'Unknown error'
