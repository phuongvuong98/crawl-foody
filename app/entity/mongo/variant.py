import mongoengine


class ProductVariant(mongoengine.Document):
    price = mongoengine.IntField(required=True)
    product_id = mongoengine.ObjectIdField(required=True)
    store_id = mongoengine.ObjectIdField(required=True)
    color_id = mongoengine.ObjectIdField(required=True)
    meta = {'allow_inheritance': True}

    def __repr__(self):
        return '<ProductVariant %r>' % (self.price)
