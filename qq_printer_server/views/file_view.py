from flask import jsonify, request
from flask_api import status
from werkzeug.utils import secure_filename
from qq_printer_server import API, DATABASE, APP
from flask_restful import Resource
from qq_printer_server.models.files import File
from qq_printer_server.serializers.file_schema import FileSchema
import os
import PyPDF2


class FilesView(Resource):
    @staticmethod
    def add_to_db(file):
        DATABASE.session.add(file)
        DATABASE.session.commit()

    @staticmethod
    def count_price(filename):
        with open(os.path.join(APP.config['UPLOAD_FOLDER'], filename), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)

            # printing number of pages in pdf file
            pages = pdf_reader.numPages
            price = pages * 0.8
            return price

    def get(self):
        pass

    def post(self):
        if 'user_id' not in request.form:
            return jsonify({
                    'message': 'There is no user id in your request'
                },
                status.HTTP_400_BAD_REQUEST
            )

        if 'file' not in request.files:
            return jsonify({
                    'message': 'There is no user id in your request'
                }, status.HTTP_400_BAD_REQUEST
            )

        user_id = request.form['user_id']
        file = request.files['file']

        filename = secure_filename(file.filename)
        price = FilesView.count_price(filename)

        file.save(os.path.join(APP.config['UPLOAD_FOLDER'], filename))

        file_model_obj = File(
            filename=filename,
            user_id=user_id,
            price=price
        )
        FilesView.add_to_db(file_model_obj)

        return jsonify(
            {
                'message': 'File was successfully added'
            },
            status.HTTP_201_CREATED
        )


class FileView(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


API.add_resource(FilesView, '/')
API.add_resource(FileView, '/<id>')
