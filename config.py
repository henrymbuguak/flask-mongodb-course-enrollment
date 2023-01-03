import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'&\xae\x07\xf9\xce\x92\xae\x1ee\x9f\xbb\xdb\x02\x1d\xf4\x1c'

    MONGODB_SETTINGS = {
        'db': 'UTA_Enrollment'
    }
