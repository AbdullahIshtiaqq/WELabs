from flask import Flask, jsonify,request, render_template
from flask_restful import Api,Resource
from database import db
from resources import  routes
import os

STATICFILES_DIRS = os.path.join('static')

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost:27017/admin'
}

api=Api(app)
db.initialize_db(app)
routes.initialize_routes(api)


@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/bookev/photography')
def photography():
    return render_template("photography.html")

@app.route('/bookev/designing')
def designing():
    return render_template("designing.html")

@app.route('/bookev/catering')
def catering():
    return render_template("catering.html")

@app.route('/bookev/decoration')
def decoration():
    return render_template("decoration.html")

@app.route('/bookev/venue')
def venues():
    return render_template("venue.html")

@app.route('/bookev/signup/service')
def registerService():
    return render_template("registerService.html")

@app.route('/bookev/signup/user')
def registerUser():
    return render_template("registerUser.html")

@app.route('/bookev/events')
def event():
    return render_template("fullEvent.html")

@app.route('/bookev/login/user')
def loginUser():
    return render_template("loginUser.html")

@app.route('/bookev/login/service')
def loginService():
    return render_template("loginService.html")

@app.route('/bookev/book/venue')
def bookVenue():
    return render_template("bookVenue.html")

@app.route('/bookev/hire/photographer')
def hirePhotographer():
    return render_template("hirePhotographer.html")

@app.route('/bookev/hire/chef')
def hireChef():
    return render_template("hireChef.html")

@app.route('/bookev/hire/designer')
def hireDesigner():
    return render_template("hireDesigner.html")

@app.route('/bookev/hire/decorator')
def hireDecorator():
    return render_template("hireDecorator.html")

@app.route('/bookev/book/event')
def bookEvent():
    return render_template("bookEvent.html")

@app.route('/bookev/myProfile')
def userProfile():
    return render_template("userProfile.html")

@app.route('/bookev/service/profile')
def serviceProfile():
    return render_template("serviceProfile.html")

@app.route('/bookev/admin')
def admin():
    return render_template("admin.html")

if __name__ == '__main__':
    app.run()
