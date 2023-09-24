import os

# Define the base config class with property for SQLALCHEMY_DATABASE_URI
class BaseConfig(object):
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        # Get database URI from enviro variables
        db = os.environ.get("DATABASE_URI")

        # Check if DATABSE_URI enviro variable is missing
        if db is None:
            raise ValueError("Missing env DATABASE_URI")
        
        return db

# Create a development configuration class that inherits from BaseConfig
class DevelopementConfig(BaseConfig):
    DEBUG=True

# Create a production configuration class
class ProductionConfig(BaseConfig):
    pass

# Create a test configuration class
class TestConfig(BaseConfig):
    pass

# Get the value of the FLASK_ENV environment variable
env = os.environ.get("FLASK_ENV")

if env == "development":
    app_config = DevelopementConfig()
elif env == "testing":
    app_config = TestConfig()
else:
    app_config = ProductionConfig()
