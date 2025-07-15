from pymongo import MongoClient
from django.conf import settings
from pydantic_mongo import AbstractRepository
from ..model.Models import CarModel

class Car_repository(AbstractRepository[CarModel]):
   def __init__(self):
        self._client = MongoClient(host=settings.DATABASE_URL)
        self._db = self._client[settings.DB_NAME]
        self._collection_name = 'car_for_rent'
        self._AbstractRepository__database = self._db
      
   class Meta:
       
      collection_name = 'car_for_rent'
         
   def get_car_paginated_results(self,page, page_size=10):
         """
         such for cars collection
         """
         collection = self.get_collection()
         skip = (page - 1) * page_size
            
            
         results = collection.find().skip(skip).limit(page_size)

         return [dict(result, _id=str(result['_id'])) for result in results]  # Convert ObjectId to str
         # def edit_car(self, car_for_rent):
         #    """
         #    Edit car
         #    """
         #    collection = self.get_collection()
         #    collection.update_one({"id": car_for_rent['id']}, {"$set": car_for_rent})
         # def delete_car(self, car_id):
         #    """
         #    Delete car by id
         #    """
         #    collection = self.get_collection()
         #    collection.delete_one({"id": car_id})