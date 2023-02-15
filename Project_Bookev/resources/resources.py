from flask import request, Response, jsonify
from flask_restful import Resource
from database.model import  User , Photographer , Chef , Designer , Decorator , Venue , FullEvent , Reviews , Booking
import json
from mongoengine import Q


class UserApi(Resource):
    def get(self):
        user = User.objects().to_json()
        return Response(user,mimetype="application/json",status=200)

    def post(self):
        body = request.get_json()
        try:
            usr = User(**body).save()
            return {'msg': 'Account Created'}, 200
        except Exception as e:
            return {'msg': 'Email already registered'}, 201

class UserLogin(Resource):
    def get(self,email):
        try:
            obj = User.objects.get(email=email).to_json();
            return Response(obj,mimetype="application/json",status=200);
        except Exception as e:
            return {'email': 'Not found'}, 201

class ServiceLogin(Resource):
    def get(self,email):
        try:
            obj = Photographer.objects.get(email=email).to_json();
            return Response(obj,mimetype="application/json",status=200)
        except Exception as e:
            try:
                obj = Chef.objects.get(email=email).to_json();
                return Response(obj, mimetype="application/json", status=200)
            except Exception as e:
                try:
                    obj = Designer.objects.get(email=email).to_json();
                    return Response(obj, mimetype="application/json", status=200)
                except Exception as e:
                    try:
                        obj = Decorator.objects.get(email=email).to_json();
                        return Response(obj, mimetype="application/json", status=200)
                    except Exception as e:
                        try:
                            obj = Venue.objects.get(email=email).to_json();
                            return Response(obj, mimetype="application/json", status=200)
                        except Exception as e:
                            return {'email': 'Not found'}, 201


class PhotographerApi(Resource):
    def get(self):
        pht = Photographer.objects().to_json()
        return Response(pht,mimetype="application/json",status=200)

    def post(self):
        body = request.get_json()
        try:
            pht= Photographer(**body).save()
            return {'msg':'Account Created'},200
        except Exception as e:
            return {'msg':'Email already registered'},201


class ChefApi(Resource):
    def get(self):
        c = Chef.objects().to_json()
        return Response(c, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        try:
            c = Chef(**body).save()
            return {'msg':'Account Created'},200
        except Exception as e:
            return {'msg':'Email already registered'},201



class DecoratorApi(Resource):
    def get(self):
        dc= Decorator.objects().to_json()
        return Response(dc, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        try:
            dc = Decorator(**body).save()
            return {'msg':'Account Created'},200
        except Exception as e:
            return {'msg':'Email already registered'},201


class DesignerApi(Resource):
    def get(self):
        ds = Designer.objects().to_json()
        return Response(ds, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        try:
            ds= Designer(**body).save()
            return {'msg':'Account Created'},200
        except Exception as e:
            return {'msg':'Email already registered'},201


class VenueApi(Resource):
    def get(self):
        v = Venue.objects().to_json()
        return Response(v, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        try:
            v = Venue(**body).save()
            return {'msg':'Account Created'},200
        except Exception as e:
            return {'msg':'Email already registered'},201

class VenueId(Resource):
    def get(self,id):
        try:
            obj = Venue.objects.get(id=id).to_json();
            return Response(obj, mimetype="application/json", status=200);
        except Exception as e:
            return {'email': 'Not found'}, 201

class PhotographerId(Resource):
    def get(self,id):
        try:
            obj = Photographer.objects.get(id=id).to_json();
            return Response(obj, mimetype="application/json", status=200);
        except Exception as e:
            return {'email': 'Not found'}, 201

class DesignerId(Resource):
    def get(self,id):
        try:
            obj = Designer.objects.get(id=id).to_json();
            return Response(obj, mimetype="application/json", status=200);
        except Exception as e:
            return {'email': 'Not found'}, 201

class DecoratorId(Resource):
    def get(self,id):
        try:
            obj = Decorator.objects.get(id=id).to_json();
            return Response(obj, mimetype="application/json", status=200);
        except Exception as e:
            return {'email': 'Not found'}, 201

class ChefId(Resource):
    def get(self,id):
        try:
            obj = Chef.objects.get(id=id).to_json();
            return Response(obj, mimetype="application/json", status=200);
        except Exception as e:
            return {'email': 'Not found'}, 201


class BookingApi(Resource):
    def get(self):
        b = Booking.objects().to_json()
        return Response(b, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        try:
            b = Booking(**body).save()
            return {'msg': 'Booking Added'}, 200
        except Exception as e:
            return {'msg': 'Operation failed'}, 201


class FullEventApi(Resource):
    def get(self):
        f = FullEvent.objects().to_json()
        return Response(f, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        f = FullEvent(**body).save()
        id = f.id
        return {'id': str(id)}, 200


class ReviewsApi(Resource):
    def get(self):
        r = Reviews.objects().to_json()
        return Response(r, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        r= Reviews(**body).save()
        id = r.id
        return {'id': str(id)}, 200
