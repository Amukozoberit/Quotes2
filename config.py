import os




class Config:
  pass
class DevelopmentConfig(Config):
    DEBUG=True
class ProductionConfig(Config):
    pass


config={
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig,
    
}