import os 

class Config: 
    '''
      General configuration parent class
      '''
 
    SECRET_KEY ='SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://barbra:reson1234@localhost/personal'

        #   email configurations
    MAIL_SERVER = 'bmootian@gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("barbra")
    MAIL_PASSWORD = os.environ.get("babimootian")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
class ProdConfig(Config):
    """Production configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # or other relevant config var
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    # rest of connection code using the connection string `uri`


class DevConfig(Config):
    """Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """

    DEBUG=True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
