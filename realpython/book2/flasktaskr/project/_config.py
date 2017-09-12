import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
# better use hdcp-genkey
SECRET_KEY = '=\x88\x07\xdd\xfa{\xe39\xdb\xffq\xdb\xcb0\xfd\x9b\x16\xf7EOm\x96;1'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)