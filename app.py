# from secrets import DATABASE_CONNECTION_URI
from flask import Flask,redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.debug = True
heroku = Heroku(app)
db = SQLAlchemy(app)

clicklink_to_weblink = {
    'tptalk':'https://www.meetup.com/PyDataChi/events/251222062/',
    'paper': 'http://arxiv.org/abs/1805.07851',
    'newsoptimism' : 'https://medium.com/@hramachandran/impact-of-linguistic-choice-of-words-in-news-articles-105122d099a5',
    'foodfda' : 'http://nbviewer.jupyter.org/github/harishaaram/Talks/blob/master/PyDataChi/Project2/PyDataChi_Project2.ipynb',
    'chicagocrime': 'http://nbviewer.jupyter.org/github/ChesterHsieh/CS-584-ML-final-project/blob/master/hsieh%28A20384559%29_ramachandran%28A20377422%29_homework1.ipynb',
    'personalwebsite':'https://harishaaram.github.io/',
    'btpersonalwebsite':'https://harishaaram.github.io/',
    'github':'https://github.com/harishaaram',
    'diagnozer':'https://www.linkedin.com/pulse/image-recognition-application-monitor-patient-harish-gandhi/',
    'thirukurral':'https://www.amazon.com/harish-Thirukurral/dp/B074CM552B/ref=sr_1_1?s=digital-skills&ie=UTF8&qid=1503190892&sr=1-1&keywords=Thirukurral',
    'mediumblog':'https://medium.com/@hramachandran',
    'bttalk': 'https://www.meetup.com/PyDataChi/events/251222062/',
}

#Many to One: https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-one

#Create our DB Model
class ClickLink(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    resume_link = db.Column(db.String(255), nullable=False)
    category_name = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime,server_default=db.func.now())
    user_agent = db.Column(db.String(255))
    platform = db.Column(db.String(255))
    browser = db.Column(db.String(255))



@app.route('/<website_link>')
def redirect_clicks(website_link='https://harishaaram.github.io/'):
    """

    :param website_link:
    :return:

    eg: www.projects.heroku.com/nlp-pydata
    resume_link = pydata and category_name = nlp

    """
    value_list = website_link.split('-')

    get_webpage= clicklink_to_weblink[value_list[1]]
    row = ClickLink(resume_link = value_list[1], category_name = value_list[0],
                    user_agent = "latency_test", platform ="latency_test",
                    browser = "latency_test")
    db.session.add(row)
    db.session.commit()
    return redirect(get_webpage,code=302)

if __name__ == "__main__":
    app.run()