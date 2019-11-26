import mongoengine


class Address(mongoengine.Document):
    detail = mongoengine.StringField(max_length=60, required=True)
    district_id = mongoengine.ObjectIdField(required=True)
    meta = {'allow_inheritance': True}

    def __repr__(self):
        return '<Address %r>' % (self.detail)
