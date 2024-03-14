import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    TEMPLATES_AUTO_RELOAD = True
   