from flask_mongoengine import Pagination
from app.entity.mongo.color import Color as ColorEntity
from app.search import query_index
from constants import Pages
from bson import ObjectId


class ColorModel(ColorEntity):
    objects = ColorEntity.objects

    def get_value_by_id(self, color_id):
        return self.objects.get(id=color_id).value

    def query_all(self):
        return self.objects

    def query_paginate(self, page):
        colors = Pagination(self.objects, int(page), int(Pages['NUMBER_PER_PAGE']))
        return colors.items, colors.pages

    def find(self, value):
        return self.objects(value__exact=value)

    def edit(self, _id, value):
        try:
            self.objects(id__exact=_id).update(set__value=value)
            return True, None
        except Exception as e:
            return False, e.__str__()

    @classmethod
    def create(cls, value):
        try:
            ColorEntity(value=value).save()
            ColorEntity.reindex()
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
        return self.value
