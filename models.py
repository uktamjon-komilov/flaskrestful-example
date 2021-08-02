from config import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    password = db.Column(db.String(255))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)

    category = db.Column(db.Integer, db.ForeignKey("category.id"))

    def serialize(self):
        data = {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

        category = Category.query.filter_by(id=int(self.category)).first()
        if category:
            data["category"] = category.serialize()

        return data



class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey("user.id"))
    is_active = db.Column(db.Boolean, default=True)


class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart = db.Column(db.Integer, db.ForeignKey("cart.id"))
    product = db.Column(db.Integer, db.ForeignKey("product.id"))
    quantity = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean)


if __name__ == "__main__":
    db.create_all()