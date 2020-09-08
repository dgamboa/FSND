import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# [x] Implement database URI and turn off track modifications
SQLALCHEMY_DATABASE_URI = 'postgresql://local-admin@localhost:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False
