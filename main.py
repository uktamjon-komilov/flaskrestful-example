from config import app, api, db

from api.category import *
from api.product import *


api.add_resource(AllCategoryResource, '/api/category/')
api.add_resource(SingleCategoryResource, '/api/category/<int:pk>/')

api.add_resource(AllProductResource, '/api/products/')
api.add_resource(SingleProductResource, '/api/product/<int:pk>/')


if __name__ == "__main__":
    app.run(debug=True)