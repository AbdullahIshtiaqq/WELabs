from .resources import BookingApi, UserLogin, ServiceLogin, ReviewsApi,ChefApi,FullEventApi,VenueApi, UserApi,PhotographerApi , DecoratorApi ,DesignerApi, VenueId, PhotographerId, DesignerId, DecoratorId, ChefId

def initialize_routes(api):
   api.add_resource(VenueId,'/api/venue/<id>')
   api.add_resource(PhotographerId, '/api/photographer/<id>')
   api.add_resource(DesignerId, '/api/designer/<id>')
   api.add_resource(DecoratorId, '/api/decorator/<id>')
   api.add_resource(ChefId, '/api/chef/<id>')
   api.add_resource(ServiceLogin,'/api/service/login/<email>')
   api.add_resource(UserLogin, '/api/user/login/<email>')
   api.add_resource(UserApi, '/api/user')
   api.add_resource(PhotographerApi, '/api/photographer')
   api.add_resource(DecoratorApi, '/api/decorator')
   api.add_resource(DesignerApi, '/api/designer')
   api.add_resource(VenueApi, '/api/venue')
   api.add_resource(ChefApi, '/api/chef')
   api.add_resource(FullEventApi, '/api/fullevent')
   api.add_resource(ReviewsApi, '/api/review')
   api.add_resource(BookingApi, '/api/booking')