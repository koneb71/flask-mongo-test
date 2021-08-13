import ast
import os

APP_NAME = os.getenv("APP_NAME", "Test Project")
SECRET_KEY = os.getenv('SECRET_KEY', "1@dErhv2Pp6B#RwR$w2M#OnE8zot#i8H7twXiZ4c2N")

MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "testproject")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")


DEBUG = ast.literal_eval(os.getenv('APP_DEBUG', 'True'))
APP_HOST = os.getenv('APP_HOST', '0.0.0.0')
APP_PORT = int(os.getenv('APP_PORT', '5000'))
