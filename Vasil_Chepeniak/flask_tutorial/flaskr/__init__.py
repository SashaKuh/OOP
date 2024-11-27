import os
from flask import Flask

def create_app(test_config=None):
    """Створює та конфігурує Flask-додаток."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Завантажує конфігурацію з config.py, якщо вона існує.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Завантажує тестову конфігурацію.
        app.config.from_mapping(test_config)

    # Створює папку instance, якщо вона не існує.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Проста сторінка привітання.
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Імпортує та ініціалізує модуль бази даних.
    from . import db
    db.init_app(app)

    # Імпортує та реєструє blueprint для аутентифікації
    from . import auth
    app.register_blueprint(auth.bp)

    # Імпортує та реєструє blueprint для блогу
    from . import blog
    app.register_blueprint(blog.bp)

    # Додає маршрут для домашньої сторінки
    app.add_url_rule('/', endpoint='index')

    return app
