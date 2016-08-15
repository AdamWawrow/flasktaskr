import os

#file containing declarations of environment variables

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'a\xce\xb3\x03\xd8h*\xfa\xad\x99\x0fu\xd8\x8d\x1ey=\xc3\x96\x7f#\xf3\x9bP'

DATABASE_PATH = os.path.join(basedir, DATABASE)
