import mongoengine


class City(mongoengine.Document):
    name = mongoengine.StringField(max_length=60, required=True, unique=True)
    meta = {'allow_inheritance': True}

    def __repr__(self):
        return '<City %r>' % (self.name)
