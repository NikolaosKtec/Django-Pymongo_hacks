
from pymongo import MongoClient
from django.conf import settings
       
class Mongo_repository():
    def __init__(self):
        
        # self._client = MongoClient(host=settings.DATABASE_URL)
        self._client = MongoClient(host=settings.DATABASE_URL)
        self._db = self._client['local']
        self._car = self._db.get_collection(name='car_for_rent')
        self._client = self._db.get_collection(name='client')

    def edit_car(self, car_for_rent):
        """
        Edit car
        """
        self._car.update_one({"id": car_for_rent['id']}, {"$set": car_for_rent})
    
    def delete_car(self, car_id):
        """
        Delete car by id
        """
        self._car.delete_one({"id": car_id})
        
    def delete_client(self, client_id):
        """
        Delete client by id
        """
        self._client.delete_one({"_id": client_id})

    def save_carForRent(self, car_for_rent):
        # obj = {
        #     # "_id": None,  # MongoDB will generate this
        #     "id": car_for_rent['id'],
        #     "vehicle": car_for_rent['vehicle'],
        #     "rent_price_month": car_for_rent['rent_price_month'],
        #     "text": car_for_rent['text'],
            
        # }
        self._car.insert_one(car_for_rent)

    def save_client(self, client):
        # obj ={
        #     # "_id": ,  # MongoDB will generate this
        #     # "id": None,
        #     "name": client['name'],
        #     "amount_pocketed": client['amount_pocketed'],
        #     "chosen_model": client['chosen_model'],
        #     "deadline_to_apply": client['deadline_to_apply'],
        #     "email": client['email'],
        #     "phone_number": client['phone_number'],
        # }
        client['deadline_to_apply'] = str(client['deadline_to_apply'])
        self._client.insert_one(client)

    def get_car_by_id(self, car_id):
        """
        Get car by id
        """
        result = self._car.find_one({"id": car_id})
        
        if result:
            # TODO Necessary line to avoid bugging the JSON serializer
            result['_id'] = str(result['_id'])
            return result
        return None

    def get_car_paginated_results(self,page_number=1, page_size=10):
        """
        such for cars collection
        """
        skip = (page_number - 1) * page_size
        
        
        results = list(self._car.find().skip(skip).limit(page_size))
        
      
        # TODO Necessary line to avoid bugging the JSON serializer
        for i in results:
            i['_id'] = str(i['_id'])
        # print(type(results[0]['_id']))

        return results  
    
    def get_client_paginated_results(self,page_number=1, page_size=10):
        """
        such for client collection
        """
        skip = (page_number - 1) * page_size
        
        
        results = list(self._client.find().skip(skip).limit(page_size))
        
      
        # TODO Necessary line to avoid bugging the JSON serializer
        for i in results:
            i['_id'] = str(i['_id'])
        # print(type(results[0]['_id']))

        return results  