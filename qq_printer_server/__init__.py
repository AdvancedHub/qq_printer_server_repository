from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


APP = Flask(__name__)
API = Api(APP)

POSTGRES = {
    'user': 'name',
    'password': 'pass',
    'database': 'db',
    'host': 'host',
    'port': 'port'
}

APP.config['DEBUG'] = True
APP.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://:' \
                                        '%(password)s@%(host)s:%(port)s' % POSTGRES

APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


DATABASE = SQLAlchemy(APP)
