from pydantic import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..model.Models import CarModel

from ..db.Car_repository import Car_repository
from pymongo.errors import DuplicateKeyError
from bson import ObjectId
class View_car(APIView):
       def get(self,request,*args, **kwargs):
              """Retrieve paginated results of cars.
              This endpoint allows you to retrieve a paginated list of cars."""
              try:
                     repo = Car_repository()
                     page = int(request.query_params.get('page'))
                     if page <= 0:
                            return Response(status=status.HTTP_400_BAD_REQUEST)
                     if page >300:
                            return Response(status=status.HTTP_400_BAD_REQUEST)
                     result = repo.get_car_paginated_results(page=page)
              except Exception as e:
                     return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
              return Response(
                     result,
                     status=status.HTTP_200_OK)

       def post(self,request):
              """Create a new car for rent.
              This endpoint allows you to create a new car by providing the necessary details."""
              repo = Car_repository()
              try:
                     validated_data = CarModel(**request.data)
                     
                     repo.save(validated_data)
                     return Response({"status": "success" },status=status.HTTP_201_CREATED)
              
              except ValidationError as e:
                     return Response({"status": "error", "errors": e.errors()}, status=400)
              except DuplicateKeyError:
                     return Response({"status": "error", "message": "Car with this ID already exists"}, status=400)

       def put(self,request):
              """Update an existing car."""
              # repo = Mongo_repository()
              repo= Car_repository()

              try:   
                     validated_data = CarModel(**request.data)
                     
                     repo.update_one({"_id": validated_data['_id']}, {"$set": validated_data})
                     return Response({"status": "success", "updated_car": validated_data.dict()})
              
              except ValidationError as e:
                     return Response({"status": "error", "errors": e.errors()}, status=400)
              except Exception as e:
                     return Response({"status": "error", "message": str(e)}, status=400)

       def delete(self):
              """Delete a car by ID."""
              repo = Car_repository()
              car_id = self.request.query_params.get('id', None)
              if not car_id:
                     return Response({"status": "error", "message": "Car ID is required"}, status=400)
              
              if not repo.find_one_by_id(ObjectId(car_id)):
                     return Response({"status": "error", "message": "Car not found"}, status=404)
              
              repo.delete_by_id(ObjectId(car_id))
              return Response({"status": "success", "message": "Car deleted successfully"}, status=200)