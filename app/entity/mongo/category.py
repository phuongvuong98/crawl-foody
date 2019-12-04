import mongoengine

from app.CRUD.search.models import SearchableMixin


class Category(mongoengine.Document, SearchableMixin):
    __tablename__ = 'category_mongo'
    __searchable__ = ['name']
    name = mongoengine.StringField(max_length=60, required=True)
    brand_id = mongoengine.ObjectIdField(required=True)
    meta = {'allow_inheritance': True}
    mysql_id = mongoengine.StringField(max_length=100)
    mysql_brand_id = mongoengine.StringField(max_length=100)

    def __repr__(self):
        return '<Category %r>' % (self.name)
