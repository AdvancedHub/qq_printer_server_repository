from qq_printer_server import API
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return '<h1>Hello world</h1>'


API.add_resource(HelloWorld, '/')
