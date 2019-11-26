import mongoengine


class Category(mongoengine.Document):
    name = mongoengine.StringField(max_length=60, required=True)
    brand_id = mongoengine.ObjectIdField(required=True)
    meta = {'allow_inheritance': True}

    def __repr__(self):
        return '<Category %r>' % (self.name)
