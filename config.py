import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Give access to the project in ANY os we find oursleves in
# Allow outside files/folders to be added to the project from the 
# Base directory

class Config():
    """
        Set Config variables for the Flask app
        Using Environment varialbles where available
        Otherwise create the config variables if not done already.
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will probably guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:080033@127.0.0.1:5432/car-collection' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turn off Update Messages from the sqlalchemy