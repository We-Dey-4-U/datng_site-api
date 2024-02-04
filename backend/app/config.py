# backend/app/config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/dating_site'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root@localhost/school-management-portal'
    