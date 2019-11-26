from flask_mongoengine import Pagination
from app.entity.mongo.city import City as CityEntity
from app.search import query_index
from constants import Pages


class CityModel(CityEntity):
    objects = CityEntity.objects

    def get_name_by_id(self, city_id):
        return self.objects.get(id=city_id).name

    def query_all(self):
        return self.objects

    def query_paginate(self, page):
        cities = Pagination(self.objects, int(page), int(Pages['NUMBER_PER_PAGE']))
        return cities.items, cities.pages

    def find_by_id(self, city_id):
        return self.objects(id__exact=city_id)

    def find(self, name):
        return self.objects(name__exact=name)

    def edit(self, _id, name):
        try:
            self.objects(id__exact=_id).update(set__name=name)
            return True, None
        except Exception as e:
            return False, e.__str__()

    @classmethod
    def create(cls, name):
        try:
            CityEntity(name=name).save()
            CityEntity.reindex()
            return True, None
        except Exception as e:
            return False, e.__str__()

    @classmethod
    def search(cls, expression, page, per_page):
        ids, obj = query_index(cls.__tablename__, expression, page, per_page)
        ids = [str(_id) for _id in ids]
        if len(obj) == 0:
            return cls.objects(id__exact=0), 0
        arr_model = []
        for _id in ids:
            try:
                arr_model.append(cls.objects.get(id=_id))
            except Exception as e:
                continue
        return arr_model, obj

    def get_value(self):
        return self.name