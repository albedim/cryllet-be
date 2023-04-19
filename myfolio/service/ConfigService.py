from resources.languages import languages


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 18/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user service
#

class ConfigService():

    @classmethod
    def getLanguages(cls):
        return languages

