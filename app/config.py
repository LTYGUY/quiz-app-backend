from os import environ as env

class Config:
    
    URI = env.get('DATABASE_URL') or 'postgresql://localhost/'
    SQLALCHEMY_DATABASE_URI = URI.replace("postgres://", "postgresql://", 1) if URI.startswith("postgres://") else URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = env.get('SECRET_KEY')
    PORT = int(env.get('PORT', 5000))