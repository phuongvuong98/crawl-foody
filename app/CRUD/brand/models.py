from flask_mongoengine import Pagination
from app.entity.mongo.brand import Brand as BrandEntity
from app.search import query_index
from constants import Pages
from bson import ObjectId


class BrandModel(BrandEntity):
    objects = BrandEntity.objects

    def get_name_by_id(self, brand_id):
        return self.objects.get(id=brand_id).name

    def query_all(self):
        return self.objects

    def query_paginate(self, page):
        cities = Pagination(self.objects, int(page), int(Pages['NUMBER_PER_PAGE']))
        return cities.items, cities.pages

    def find(self, name):
        return self.objects(name__exact=name)

    def find_by_id(self, brand_id):
        return self.objects(id__exact=brand_id)

    def edit(self, _id, name):
        try:
            self.objects(id__exact=_id).update(set__name=name)
            return True, None
        except Exception as e:
            return False, e.__str__()

    @classmethod
    def create(cls, name):
        try:
            BrandEntity(name=name).save()
            BrandEntity.reindex()
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
