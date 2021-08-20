import os




class Config:
  pass
class DevelopmentConfig(Config):
    DEBUG=True
class ProductionConfig(Config):
    pass


config_options={
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig,
    
}