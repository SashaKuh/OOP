import sqlite3
import click
from flask import current_app, g
from datetime import datetime


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Очистити існуючі дані і створити нові таблиці."""
    init_db()
    click.echo('База даних ініціалізована.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


# Реєструємо конвертер для роботи з датами
sqlite3.register_converter('timestamp', lambda x: datetime.fromisoformat(x.decode())) 