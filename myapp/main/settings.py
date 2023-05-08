import pathlib
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

SECRET_KEY = os.urandom(36)
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
p = pathlib.Path('users.db')
engine = create_engine('sqlite:///'+str(p), echo=True)
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

Session = sessionmaker(bind=engine)
session = Session()


UPLOAD_FOLDER = os.path.join(basedir, 'users')
