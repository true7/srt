from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(value):
    url_validation = URLValidator(message='Invalid URL')
    url_validation(value)
    return value
