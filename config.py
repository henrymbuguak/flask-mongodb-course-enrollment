import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PBO9QeqJeuaD2/xtilmmfw=='

    MONGODB_SETTINGS = {
        'db': 'UTA_Enrollment'
    }
