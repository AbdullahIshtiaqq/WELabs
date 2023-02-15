from .resources import  ProductInsert,ProductGet,ProductUpdate,ProductDelete,ProductSearch

def initialize_routes(api):
   api.add_resource(ProductInsert, '/api/productInsert')
   api.add_resource(ProductGet, '/api/productGet', '/api/productGet/<num>')
   api.add_resource(ProductUpdate, '/api/productUpdate/<id>')
   api.add_resource(ProductDelete, '/api/productDelete/<id>')
   api.add_resource(ProductSearch, '/api/productSearch/<key>')
