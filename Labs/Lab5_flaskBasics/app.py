from flask import Flask, render_template, request,session,make_response
from flask_session import Session
from controller import ContactController

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["SECRET_KEY"]
Session(app)

app = Flask(__name__)

@app.route('/mainMenu')
def menu():
    if session['email'] == None:
        return render_template("login.html",msg="Enter your credentials.")
    return render_template("MainMenu.html")

@app.route('/addContact')
def addContact():
    return render_template("create_contact.html",msg="Enter Details in the fields")

@app.route('/addContact/extractData', methods = ["POST"])
def extractData():
    name = request.form['name']
    mobileno = request.form['mobileno']
    city = request.form['city']
    profession = request.form['profession']
    controller = ContactController()
    if controller.addContact(name,mobileno,city,profession):
        return render_template("create_contact.html",msg="Contact added")
    else:
        return render_template("create_contact.html",msg="Couldn't add contact")

@app.route('/searchContact')
def searchContact():
    return render_template("contact.html",msg="")

@app.route('/searchContact/getContact', methods = ["POST"])
def getContact():
    name = request.form['name']
    controller = ContactController()
    contact = controller.getContact(name)
    if contact == None:
        return render_template("contact.html",msg="Contact Not Found")
    else:
        return render_template("displayContact.html",name = contact.name, mobileno = contact.mobileno, city = contact.city, profession = contact.profession)

@app.route('/displayContacts')
def displayAllContacts():
    controller = ContactController()
    myList = controller.getAllContacts()
    return render_template("displayContactsTable.html", contacts=myList)

@app.route('/')
def signup():
    return render_template("signup.html")

@app.route('/signup/getData', methods=["POST"])
def getSignUpForm():
    email=request.form['email']
    password=request.form['password']
    controller = ContactController()
    if controller.validateUser(email,password):
        return render_template("mainMenu.html")
    else:
        return render_template("signup.html")

@app.route('/login')
def login():
    return render_template("login.html", msg="Enter your credentials")

@app.route('/login/getData', methods=["POST"])
def getLoginForm():
    email=request.form['email']
    password=request.form['password']
    controller = ContactController()
    if not controller.isUserPresent(email):
        return render_template("login.html", msg="Email not registered.")

    if controller.authorize(email,password):
        return render_template("mainMenu.html")
    else:
        return render_template("login.html", msg="Incorrect Password.")

@app.route('/logout')
def logout():
    session.clear()
    return render_template("login.html", msg="Enter your credentials")

if __name__ == '__main__':
    app.run()