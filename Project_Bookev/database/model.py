from .db import db

class User(db.Document):
    name = db.StringField(required=True)
    cnic = db.StringField(required=True)
    mobileNo = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)

class Photographer(db.Document):
    name = db.StringField(required=True)
    cnic = db.StringField(required=True)
    mobileNo = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    hourlyRate=db.DecimalField(required=True)
    portfolio=db.StringField(required=True)
    speciality=db.StringField(required=True)

class Chef(db.Document):
    name = db.StringField(required=True)
    cnic = db.StringField(required=True)
    mobileNo = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    experience=db.IntField(required=True)
    speciality=db.StringField(required=True)
    charges=db.DecimalField(required=True)

class Designer(db.Document):
    name = db.StringField(required=True)
    cnic = db.StringField(required=True)
    mobileNo = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    experience=db.IntField(required=True)
    speciality=db.StringField(required=True)
    charges=db.DecimalField(required=True)
    maxLimit=db.IntField(required=True)


class Decorator(db.Document):
    name = db.StringField(required=True)
    cnic = db.StringField(required=True)
    mobileNo = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    experience=db.IntField(required=True)
    speciality=db.StringField(required=True)
    charges=db.DecimalField(required=True)


class Venue(db.Document):
    name = db.StringField(required=True)
    cnic = db.StringField(required=True)
    mobileNo = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    address = db.StringField(required=True)
    capacity= db.IntField(required=True)
    charges = db.DecimalField(required=True)

class FullEvent(db.Document):
    startTime = db.StringField(required=True)
    endTime = db.StringField(required=True)
    date = db.StringField(required=True)
    description = db.StringField(required=True)
    userMail = db.StringField(required=True)

class Booking(db.Document):
    startTime = db.StringField(required=True)
    endTime = db.StringField(required=True)
    date = db.StringField(required=True)
    charges = db.DecimalField(required=True)
    userMail = db.StringField(required=True)
    serviceMail = db.StringField(required=True)

class Reviews(db.Document):
    feedback = db.StringField(required=True)
    userMail = db.StringField(required=True)
    serviceMail = db.StringField(required=True)