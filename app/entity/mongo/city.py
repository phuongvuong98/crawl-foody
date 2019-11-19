import mongoengine


class City(mongoengine.Document):
    name = mongoengine.StringField(max_length=60)
    meta = {'allow_inheritance': True}

    def __repr__(self):
        return '<City %r>' % (self.name)
