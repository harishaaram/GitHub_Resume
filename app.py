# from secrets import DATABASE_CONNECTION_URI
from flask import Flask,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.debug = True
heroku = Heroku(app)
db = SQLAlchemy(app)



#Many to One: https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-one

#Create our DB Model
class ClickLink(db.Model):
    link_id = db.Column(db.Integer,nullable=False)
    resume_link = db.Column(db.String(255), primary_key=True)
    category_name = db.Column(db.String(255), nullable=False)
    click_count = db.Column(db.Integer, default = 0)

    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

class OriginalLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    web_link = db.Column(db.String(255), unique=True, nullable=False)

    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

@app.route('/')
def redirect_clicks(website_link='https://harishaaram.github.io/'):
    return redirect(website_link,code=302)

if __name__ == "__main__":
    app.run()