import re
from os.path import join, dirname

from setuptools import setup, find_packages


with open(join(dirname(__file__), 'wizard_router', '__init__.py')) as v_file:
    package_version = re.compile('.*__version__ = \'(.*?)\'', re.S).\
        match(v_file.read()).group(1)


dependencies = [
    'restfulpy >= 3.4.0, < 4',
    'requests',
    'sqlalchemy_media',

    # Deployment
    'gunicorn',
]


setup(
    name='wizard-router',
    version=package_version,
    packages=find_packages(),
    install_requires=dependencies,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'wizard_router = wizard_router:wizard_router.cli_main'
        ]
    }
)

