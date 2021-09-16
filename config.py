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
    # SQLALCHEMY_DATABASE_URI = 'postgresql://dwezvsaeimqmtx:65f6f348f287360f900cd1ff7cde19229bc4440612b470173f571452c3d24600@ec2-54-146-84-101.compute-1.amazonaws.com:5432/df0cvg2anf52d3' 
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:080033@127.0.0.1:5432/car-collection'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turn off Update Messages from the sqlalchemy