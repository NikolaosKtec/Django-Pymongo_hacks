from pymongo import MongoClient
from django.conf import settings
from pydantic_mongo import AbstractRepository
from ..model.Models import ContractModel

class Contract_repository(AbstractRepository[ContractModel]):
   def __init__(self):
        self._client = MongoClient(host=settings.DATABASE_URL)
        self._db = self._client[settings.DB_NAME]
        self._collection_name = 'contract'
        self._AbstractRepository__database = self._db
      
   class Meta:
       
      collection_name = 'contract'
         
   def get_contract_paginated_results(self,page, page_size=10):
         """
         such for contract collection
         """
         collection = self.get_collection()
         skip = (page - 1) * page_size
            
            
         results = collection.find().skip(skip).limit(page_size)

         results = [dict(result, _id=str(result['_id'])) for result in results]  # Convert ObjectId to str
         results = [dict(result, id_client=str(result['id_client'])) for result in results]  # Convert ObjectId to str
         results = [dict(result, id_car=str(result['id_car'])) for result in results]  # Convert ObjectId to str
         return results