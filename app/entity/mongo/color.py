import mongoengine


class Color(mongoengine.Document):
    value = mongoengine.StringField(max_length=50, required=True, unique=True)
    meta = {'allow_inheritance': True}

    def __repr__(self):
        return '<Color %r>' % (self.value)
