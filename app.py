from flask_jwt_extended import JWTManager

from cryllet.configuration.config import app, sql#, scheduler
from cryllet.controller import UserController, CryllinkController, CrylletStatsController
from cryllet.service.AsyncService import AsyncService
from cryllet.utils.Utils import Utils

# controllers init
app.register_blueprint(CryllinkController.cryllink)
app.register_blueprint(CrylletStatsController.crylletStats)
app.register_blueprint(UserController.user)

# modules init
JWTManager(app)


def create_app():
    with app.app_context():
        sql.create_all()
        # scheduler.start()
        # scheduler.add_job(id=Utils.createLink(5), func=AsyncService.checkExpiration, trigger='interval', seconds=86400)
    return app


if __name__ == '__main__':
    create_app().run()