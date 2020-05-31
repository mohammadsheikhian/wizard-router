import base64

from restfulpy.orm import DBSession

from .models import Member


def insert(): # pragma: no cover
    admin = Member(
        title='GOD',
        first_name='First name',
        last_name='Last name',
        email='god@example.com',
        password='123456',
    )
    DBSession.add(admin)
    DBSession.commit()

    print('Admin has been created.')
    print(
        f'  Title: {admin.title}\n'
        f'  First Name: {admin.first_name}\n'
        f'  Last Name: {admin.last_name}\n'
        f'  Email: {admin.email}\n'
        f'  Password: 123456\n'
    )

