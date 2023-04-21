from flask_jwt_extended import JWTManager

from myfolio.configuration.config import app, sql
from myfolio.controller import UserController, ConfigController, LanguageController, SkillController, \
    PortfolioController

# controllers init
app.register_blueprint(ConfigController.config)
app.register_blueprint(PortfolioController.portfolio)
app.register_blueprint(SkillController.skill)
app.register_blueprint(LanguageController.language)
app.register_blueprint(UserController.user)

# modules init
JWTManager(app)


def create_app():
    with app.app_context():
        sql.create_all()
    return app


if __name__ == '__main__':
    create_app().run()