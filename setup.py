from setuptools import setup, find_packages

setup(
    name='exchange_calendars',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    author='mwz',
    author_email='gerrymanoim@gmail.com',
    description='Python library for exchange trading calendars',
    url='https://github.com/muwazana/exchange_calendars.git',
)