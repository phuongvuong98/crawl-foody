import mongoengine


class District(mongoengine.Document):
    name = mongoengine.StringField(max_length=60, required=True)
    city_id = mongoengine.ObjectIdField(required=True)
    meta = {'allow_inheritance': True}

    def __repr__(self):
        return '<District %r>' % (self.name)
