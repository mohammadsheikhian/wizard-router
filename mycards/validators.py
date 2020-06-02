import re

from nanohttp import validate, HTTPStatus, context, int_or_notfound, \
    HTTPBadRequest
from restfulpy.orm import DBSession
from restfulpy.datetimehelpers import parse_datetime

from .exceptions import *
from .models import *


USER_EMAIL_PATTERN = re.compile(
    r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
)


email_validator = validate(
    email=dict(
        required='400 Email Not In Form',
        pattern=(USER_EMAIL_PATTERN, '400 Invalid Email Format')
    )
)

