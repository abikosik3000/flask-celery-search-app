from the_finder import app
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["BASEDIR"] = basedir

app.config["SEARCH_DIRECTORY"] = "/home/abikosik3000/var/www/search_app/test_repo"

#sqlalhemy
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
