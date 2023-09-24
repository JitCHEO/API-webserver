
# Set the Flask run port to 4000
FLASK_RUN_PORT=4000

'main' is the name of the module, and 'init_app' is the function that initializes the Flask app.
FLASK_APP=main:init_app

# Setting Flask environment to 'development'
# This typically means the application is in development mode.
FLASK_ENV=development

# Enable Flask debugging mode
# When debugging is enabled, Flask provides more detailed error messages in case of issues.
FLASK_DEBUG=True