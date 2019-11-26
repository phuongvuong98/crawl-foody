import mongoengine


class Product(mongoengine.Document):
    name = mongoengine.StringField(max_length=60, required=True)
    category_id = mongoengine.ObjectIdField(required=True)
    meta = {'allow_inheritance': True}

    def __repr__(self):
        return '<Address %r>' % (self.name)
