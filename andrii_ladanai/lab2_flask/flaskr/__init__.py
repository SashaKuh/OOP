import os
from flask import Flask

def create_app(test_config=None):
    # створюємо та налаштовуємо додаток
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # встановлюємо стандартні налаштування
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # завантажуємо конфігурацію екземпляра, якщо вона існує
        app.config.from_pyfile('config.py', silent=True)
    else:
        # завантажуємо тестову конфігурацію
        app.config.update(test_config)

    # переконуємося, що папка екземпляра існує
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # проста сторінка для перевірки
    @app.route('/hello')
    def hello():
        return 'Привіт, Світ!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app 