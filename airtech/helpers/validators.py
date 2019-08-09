import re
from rest_framework.serializers import ValidationError


class Validators(object):

    def is_valid_password(self, password):
        if not re.match(r'^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).*', password):  # noqa E501
            raise ValidationError(
                'Password must contain a number, capital letter and special charachter'  # noqa E501
            )
        return password

    def is_valid_string(self, string, entity):
        if not re.findall(r'[A-Za-z]', string):
            raise ValidationError(
                f'{entity} cannot contain numbers or special characters only'
            )
        return string
