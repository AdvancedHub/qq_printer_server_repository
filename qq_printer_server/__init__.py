from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import os


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
APP.config['UPLOAD_FOLDER'] = os.path.abspath('uploaded_files')

APP.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://%(user)s:' \
                                        '%(password)s@%(host)s:%(port)s/%(database)s' % POSTGRES

APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DATABASE = SQLAlchemy(APP)
MARSHMALLOW = Marshmallow(APP)
MIGRATE = Migrate(APP, DATABASE)
MANAGER = Manager(APP)
MANAGER.add_command('db', MigrateCommand)
