import mongoengine


class Store(mongoengine.Document):
    store_name = mongoengine.StringField(max_length=60, required=True)
    address_id = mongoengine.ObjectIdField(required=True)
    meta = {'allow_inheritance': True}

    def __repr__(self):
        return '<Store %r>' % (self.store_name)
