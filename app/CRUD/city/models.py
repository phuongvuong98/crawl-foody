import math

from flask_mongoengine import Pagination

from app import db
from app.entity.mongo.city import City as CityEntity
from constants import Pages


class City(CityEntity):
    __tablename__ = 'city'

    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        try:
            CityEntity(name=name).save()
            return True
        except:
            return False

    @classmethod
    def edit(cls, _id, name):
        try:
            CityEntity.objects(id__exact=_id).update(set__name=name)
            return True, None
        except:
            return False, "Your city is existed"

    @classmethod
    def find(cls, name):
        print(CityEntity.objects(name__exact=name))
        return CityEntity.objects(name__exact=name)

    @classmethod
    def query_all(cls, page):
        cities = Pagination(CityEntity.objects, int(page), int(Pages['NUMBER_PER_PAGE']))
        return cities.items, cities.pages
