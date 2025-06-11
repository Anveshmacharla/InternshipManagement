import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:0520@localhost/internship_management_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecretkey'