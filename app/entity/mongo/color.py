import mongoengine

from app.CRUD.search.models import SearchableMixin


class Color(mongoengine.Document, SearchableMixin):
    __tablename__ = 'color_mongo'
    __searchable__ = ['value']
    value = mongoengine.StringField(max_length=50, required=True, unique=True)
    meta = {'allow_inheritance': True}
    mysql_id = mongoengine.StringField(max_length=100)
    def __repr__(self):
        return '<Color %r>' % (self.value)
