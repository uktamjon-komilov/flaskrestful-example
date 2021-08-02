from config import app, api, db

from api.category.all import AllCategoryResource
from api.category.single import SingleCategoryResource



api.add_resource(AllCategoryResource, '/api/category/')
api.add_resource(SingleCategoryResource, '/api/category/<int:pk>/')

if __name__ == "__main__":
    app.run(debug=True)


# GET, POST:
# /api/products/

# GET, PUT, PATCH, DELETE
# /api/products/1/