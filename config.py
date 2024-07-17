import os

class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY', 'supersecretkey')
        MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/mydatabase')

