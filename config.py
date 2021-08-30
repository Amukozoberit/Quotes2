import os




class Config:
  # SECRET_KEY=os.getenv.get('SECRET_KEY')
  SECRET_KEY='rE\x1eKQ\xa0\x80\xee\xa2\xfcf{\xb9Ki&'
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://mwashe:github2122@localhost/quotesa'
  QUOTES_URL='http://quotes.stormconsultancy.co.uk/random.json'
#   SECRET_KEY=os.environ.get('SECRET_KEY')
  MAIL_SERVER = 'smtp.gmail.com'
  MAIL_PORT = 465
  MAIL_USE_TLS = False
  MAIL_USE_SSL = True
  MAIL_USERNAME ='mwasheberit@gmail.com'
  MAIL_PASSWORD ='github2122'
  UPLOADED_PHOTOS_DEST='app/static/photos'

class DevelopmentConfig(Config):
    DEBUG=True
class ProductionConfig(Config):
    pass


config_options={
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig,
    
}