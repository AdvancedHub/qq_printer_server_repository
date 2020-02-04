from qq_printer_server import DATABASE
from datetime import datetime


class File(DATABASE.Model):
    __tablename__ = 'files'

    id = DATABASE.Column(DATABASE.INTEGER, primary_key=True, unique=True)
    filename = DATABASE.Column(DATABASE.VARCHAR, nullable=False)
    user_id = DATABASE.Column(DATABASE.INTEGER, nullable=False)
    datetime = DATABASE.Column(DATABASE.DateTime, default=datetime.now(), nullable=False)
    price = DATABASE.Column(DATABASE.Numeric(precision=2, asdecimal=False, decimal_return_scale=False), nullable=False)
    payment = DATABASE.Column(DATABASE.Boolean, default=False)

    def __init__(self, filename, user_id, price):
        self.filename = filename
        self.user_id = user_id
        self.datetime = datetime.now()
        self.price = price
        self.payment = False
