from flask import Flask, jsonify,request, render_template
from flask_restful import Api,Resource
from database import db
from resources import  routes


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost:27017/admin'
}
api=Api(app)
db.initialize_db(app)
routes.initialize_routes(api)

@app.route('/')
def menu():
    return render_template("homepage.html")

@app.route('/add')
def addProduct():
    return render_template("addProduct.html")

@app.route('/show')
def showProducts():
    return render_template("showProducts.html")

@app.route('/update')
def updateProduct():
    return render_template("updateProduct.html")

@app.route('/delete')
def deleteProduct():
    return render_template("deleteProduct.html")

@app.route('/search')
def searchProducts():
    return render_template("searchProduct.html")


if __name__ == '__main__':
    app.run()
