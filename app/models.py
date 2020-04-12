from flask_mongoengine import Pagination
from entity.foody import Foody as FoodyEntity


class FoodyModel(FoodyEntity):
    objects = FoodyEntity.objects

    def get_name_by_id(self, Foody_id):
        return self.objects.get(id=Foody_id).name

    def query_all(self):
        return self.objects

    def query_paginate(self, page):
        cities = Pagination(self.objects, int(page), 10)
        return cities.items, cities.pages

    def find_by_id(self, Foody_id):
        return self.objects(id__exact=Foody_id)

    def find(self, name):
        return self.objects(name__exact=name)

    def edit(self, _id, name):
        try:
            self.objects(id__exact=_id).update(set__name=name)
            FoodyEntity.reindex()
            return True, None
        except Exception as e:
            return False, e.__str__()

    @classmethod
    def create(cls, name):
        try:
            FoodyEntity(name=name).save()
            FoodyEntity.reindex()
            return True, None
        except Exception as e:
            return False, e.__str__()