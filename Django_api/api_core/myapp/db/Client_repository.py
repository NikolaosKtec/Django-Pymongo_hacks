from pymongo import MongoClient
from django.conf import settings
from pydantic_mongo import AbstractRepository
from ..model.Models import ClientModel

class Client_repository(AbstractRepository[ClientModel]):
   def __init__(self):
        self._client = MongoClient(host=settings.DATABASE_URL)
        self._db = self._client[settings.DB_NAME]
        self._collection_name = 'client'
        self._AbstractRepository__database = self._db
      
   class Meta:
       
      collection_name = 'client'
         
   def get_client_paginated_results(self,page, page_size=10):
         """
         such for client collection
         """
         collection = self.get_collection()
         skip = (page - 1) * page_size
            
            
         results = collection.find().skip(skip).limit(page_size)

         return [dict(result, _id=str(result['_id'])) for result in results]  # Convert ObjectId to str