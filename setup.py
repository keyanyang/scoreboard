from distutils.core import setup
from setuptools import setup

setup(
    name='scoreboard',
    packages=['scoreboard'],
    version='0.0.0',
    description='Checking live scores in terminal',
    url='https://github.com/keyanyang/scoreboard',
    entry_points={
          'console_scripts': [
              'live = live:main'
          ]
    },
)
