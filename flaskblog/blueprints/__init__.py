from flaskblog.blueprints.users.routes import users
from flaskblog.blueprints.posts.routes import posts
from flaskblog.blueprints.main.routes import main
from flaskblog.blueprints.errors.handlers import errors


def init_app(app):
    
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app