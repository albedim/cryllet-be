from myfolio.model.entity.Like import Like
from myfolio.model.repository.LikeRepository import LikeRepository
from myfolio.model.repository.ProjectRepository import ProjectRepository
from myfolio.model.repository.UserRepository import UserRepository
from myfolio.service.UserPermissionService import UserPermissionService
from myfolio.utils.Constants import Constants
from myfolio.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 21/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the project service
#

class ProjectService():

    @classmethod
    def add(cls, request):
        if not UserPermissionService.canAddProjectToPortfolio(request['user_id'], request['portfolio_id']):
            return Utils.createWrongResponse(False, Constants.NOT_ENOUGH_PERMISSIONS, 306), 306
        else:
            ProjectRepository.add(request['title'], request['description'], request['portfolio_id'])
            return Utils.createSuccessResponse(True, Constants.CREATED)

    @classmethod
    def getProjects(cls, portfolioId):
        projects = ProjectRepository.getProjects(portfolioId)
        result = []
        for project in projects:
            result.append(project.toJson())
        return result

    @classmethod
    def getProject(cls, requestUserId, projectId):
        requestUser = UserRepository.getUserById(requestUserId)
        project = ProjectRepository.getProject(projectId)
        like: Like = LikeRepository.get(requestUserId, projectId)
        likes: int = len(LikeRepository.getLikes(projectId))
        unlikes: int = len(LikeRepository.getUnlikes(projectId))
        return project.toJson_Editable_Liked(
            requestUser.user_id == project.user_id if requestUser is not None else False,
            {'likes': likes, 'unlikes': unlikes, 'liked': like.liked, 'unliked': like.unliked} \
                if like is not None else {'liked': False, 'unliked': False, 'likes': likes, 'unlikes': unlikes}
        )
