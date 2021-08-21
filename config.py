import os




class Config:
  SECRET_KEY='rE\x1eKQ\xa0\x80\xee\xa2\xfcf{\xb9Ki&'
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://mwashe:github2122@localhost/quotesa'
  QUOTES_URL='http://quotes.stormconsultancy.co.uk/random.json'
class DevelopmentConfig(Config):
    DEBUG=True
class ProductionConfig(Config):
    pass


config_options={
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig,
    
}