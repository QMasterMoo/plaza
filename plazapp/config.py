import os

APPLICATION_ROOT = '/'

SECRET_KEY = b'\xfb\x1d\x8a\x92\xb1\xc1\xc4\xb8\xf6{\xef\n\xa3\xd4L\x86\xb9\x81\x1e\xbb\xc3\x1d\xb9\xc8'
SESSION_COOKIE_NAME = 'login'

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data', 'uploads')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGHT = 16*1024*1024

DATABASE_FILENAME = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data', 'plazapp.sqlite3')