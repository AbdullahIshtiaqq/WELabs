from flask import request, Response, jsonify
from flask_restful import Resource
from database.models import Product
import json

class ProductInsert(Resource):
    def post(self):
        body = request.get_json()
        try:
            prod = Product(**body).save()
            if prod.name == "" or prod.description == "" or prod.price == None:
                raise Exception
            id = prod.id
            return {'msg':'Product Added Successfully!'},200
        except Exception as e:
            return{'msg':'Invalid data sent!'},201


class ProductGet(Resource):
    def get(self,num = None):
        try:
            if int(num) < 0:
                return {'msg':'Invalid argument sent'},201
        except Exception as e:
            if num != None:
                return {'msg': 'Invalid argument sent'}, 201

        products = []
        temp = Product.objects().to_json()
        if num == None:
            products = temp
        else:
            list = json.loads(temp)
            i = 0
            tempProd = []
            for i in range(int(num)):
                try:
                    tempProd.append(list[i])
                except Exception as e:
                    i = int(num)
            products = json.dumps(tempProd)

        return Response(products, mimetype="application/json", status=200)


class ProductUpdate(Resource):
    def put(self,id):
        body = request.get_json()
        try:
            Product.objects.get(id=id).update(**body)
            return Response(Product.objects.get(id=id).to_json(), mimetype="application/json",status=200)
        except Exception as e:
            return {'msg':'Update failed. Please check id or arguments sent.'},201

class ProductDelete(Resource):
    def delete(self, id):
        try:
            Product.objects.get(id=id).delete()
            return Response({'msg':'Record deleted successfully.'}, status=200)
        except Exception as e:
            return Response({'msg':'Record not found'}, status=404)

class ProductSearch(Resource):
    def get(self,key):
        result = []
        temp = Product.objects().to_json()
        list = json.loads(temp)
        for item in list:
            print(item)
            print(type(item))
            if key in item["name"] or key in item["description"]:
                result.append(item)
        temp = json.dumps(result)
        return Response(temp,mimetype="application/json",status=200)