import os
import uuid
from hashlib import sha256
from datetime import datetime

from nanohttp import context, settings, HTTPStatus
from restfulpy.orm import DeclarativeBase, Field, DBSession, relationship
from restfulpy.principal import JWTRefreshToken, JWTPrincipal
from sqlalchemy import Unicode, Integer, JSON, Date, UniqueConstraint, String
from sqlalchemy.orm import synonym
from sqlalchemy_media import Image, ImageAnalyzer, ImageValidator, \
    MagicAnalyzer, ContentTypeValidator
from sqlalchemy_media.constants import KB
from sqlalchemy_media.exceptions import DimensionValidationError, \
    AspectRatioValidationError, MaximumLengthIsReachedError, \
    ContentTypeValidationError


AVATAR_CONTENT_TYPES = ['image/jpeg', 'image/png']


class Avatar(Image):

    _internal_max_length = None
    _internal_min_length = None

    __pre_processors__ = [
        MagicAnalyzer(),
        ContentTypeValidator([ 'image/jpeg', 'image/png', ]),
        ImageAnalyzer(),
        ImageValidator(
            minimum=(200, 200),
            maximum=(300, 300),
            min_aspect_ratio=1,
            max_aspect_ratio=1,
            content_types=AVATAR_CONTENT_TYPES
        ),
    ]

    __prefix__ = 'avatar'

    @property
    def __max_length__(self):
        if self._internal_max_length is None:
            self._internal_max_length = \
                settings.attachments.members.avatars.max_length * KB

        return self._internal_max_length

    @__max_length__.setter
    def __max_length__(self, v):
        self._internal_max_length = v

    @property
    def __min_length__(self):
        if self._internal_min_length is None:
            self._internal_min_length = \
                settings.attachments.members.avatars.min_length * KB

        return self._internal_min_length

    @__min_length__.setter
    def __min_length__(self, v):
        self._internal_min_length = v


class Member(DeclarativeBase):
    __tablename__ = 'member'

    id = Field(Integer, primary_key=True)

    email = Field(
        Unicode(100),
        unique=True,
        index=True,
        min_length=7,
        max_length=100,
        pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        pattern_description='Invalid email format, example: user@example.com',
        python_type=str,
        not_none=True,
        required=True,
        watermark=None,
        example='user@example.com',
        label='Email Address',
        message=None,
    )
    title = Field(
        Unicode(100),
        unique=True,
        pattern=r'^[a-zA-Z][\w]{5,19}$',
        pattern_description='Username can only include alphanumeric characters'
            'and underscore',
        python_type=str,
        not_none=True,
        required=True,
        min_length=6,
        max_length=20,
        example='John_Doe',
        watermark=None,
        label='Username',
        message=None,
    )
    first_name = Field(
        Unicode(20),
        nullable=False,
        not_none=True,
        python_type=str,
        min_length=3,
        max_length=20,
        required=True,
        pattern=r'^[a-zA-Z]{1}[a-z-A-Z ,.\'-]{2,19}$',
        pattern_description='Only alphabetical characters, ., \' and space are'
            'valid',
        example='John',
        label='First Name',
        watermark=None,
        message=None,
    )
    last_name = Field(
        Unicode(20),
        nullable=False,
        not_none=True,
        python_type=str,
        min_length=3,
        max_length=20,
        required=True,
        pattern=r'^[a-zA-Z]{1}[a-z-A-Z ,.\'-]{2,19}$',
        pattern_description='Only alphabetical characters, ., \' and space are'
            'valid',
        example='Doe',
        label='Last Name',
        watermark=None,
        message=None,
    )
    phone = Field(
        Unicode(16),
        nullable=True,
        not_none=False,
        unique=True,
        pattern=r'^[+]{0,1}[\d+]{7,15}$',
        pattern_description='Lorem ipsum dolor sit amet',
        python_type=str,
        required=False,
        min_length=8,
        max_length=16,
        watermark=None,
        label='Phone Number',
        example='1234567',
    )
    _avatar = Field(
        'avatar',
        Avatar.as_mutable(JSON),
        nullable=True,
        protected=False,
        json='avatar',
        not_none=False,
        label='Avatar',
        required=False,
    )
    _password = Field(
        'password',
        Unicode(128),
        index=True,
        protected=True,
        json='password',
        pattern=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).+$',
        pattern_description='Password must include at least one uppercase, one'
            'lowercase and one number',
        example='ABCabc123',
        watermark=None,
        label='Password',
        message=None,
        min_length=6,
        max_length=20,
        required=True,
        python_type=str,
        not_none=True,
    )

    @property
    def avatar(self):
        return self._avatar.locate() if self._avatar else None

    @avatar.setter
    def avatar(self, value):
        if value is not None:
            try:
                self._avatar = Avatar.create_from(value)

            except DimensionValidationError as e:
                raise HTTPStatus(f'618 {e}')

            except AspectRatioValidationError as e:
                raise HTTPStatus(
                    '619 Invalid aspect ratio Only 1/1 is accepted.'
                )

            except ContentTypeValidationError as e:
                raise HTTPStatus(
                    f'620 Invalid content type, Valid options are: '\
                    f'{", ".join(type for type in AVATAR_CONTENT_TYPES)}'
                )

            except MaximumLengthIsReachedError as e:
                max_length = settings.attachments.members.avatars.max_length
                raise HTTPStatus(
                    f'621 Cannot store files larger than: '\
                    f'{max_length * 1024} bytes'
                )

        else:
            self._avatar = None

    def _hash_password(cls, password):
        salt = sha256()
        salt.update(os.urandom(60))
        salt = salt.hexdigest()

        hashed_pass = sha256()
        # Make sure password is a str because we cannot hash unicode objects
        hashed_pass.update((password + salt).encode('utf-8'))
        hashed_pass = hashed_pass.hexdigest()

        password = salt + hashed_pass
        return password

    def _set_password(self, password):
        """Hash ``password`` on the fly and store its hashed version."""
        self._password = self._hash_password(password)

    def _get_password(self):
        """Return the hashed version of the password."""
        return self._password

    password = synonym(
        '_password',
        descriptor=property(_get_password, _set_password),
        info=dict(protected=True)
    )

    def create_jwt_principal(self):
        return JWTPrincipal({
            'id': self.id,
            'email': self.email,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'title': self.title,
            'avatar': self.avatar,
            'sessionId': str(uuid.uuid4()),
        })

    def create_refresh_principal(self):
        return JWTRefreshToken(dict(id=self.id))

    def validate_password(self, password):
        hashed_pass = sha256()
        hashed_pass.update((password + self.password[:64]).encode('utf-8'))

        return self.password[64:] == hashed_pass.hexdigest()

    def __repr__(self):
        return f'Member: {self.id} {self.title} {self.email}'

