from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#Initializing Flask instance
app= Flask(__name__)

#Database url
DATABASE_URL = ""

#Config settings for the app 
# or 
# You can create Config file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#Initialize database for flask app
db= SQLAlchemy(app)


from StringParser import urls
from StringParser import utils

