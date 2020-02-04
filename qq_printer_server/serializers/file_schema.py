from qq_printer_server import MARSHMALLOW
from qq_printer_server.models.files import File


class FileSchema(MARSHMALLOW.ModelSchema):
    class Meta:
        model = File


FILE_SCHEMA = FileSchema()
