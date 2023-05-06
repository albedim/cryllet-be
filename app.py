from flask_jwt_extended import JWTManager

from cryllet.configuration.config import app, sql
from cryllet.controller import UserController, CryllinkController

# controllers init
app.register_blueprint(CryllinkController.cryllink)
app.register_blueprint(UserController.user)

# modules init
JWTManager(app)


def create_app():
    with app.app_context():
        sql.create_all()
    return app


if __name__ == '__main__':
    create_app().run()