from pydantic import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..data.DataFormAbstract import CarValidator

from ..db.Mongo_repository import Mongo_repository
from pymongo.errors import DuplicateKeyError

class View_car(APIView):
       def get(self,request,page_number=1,*args, **kwargs):
              """Retrieve paginated results of cars."""
              repo = Mongo_repository()

              if page_number <= 0:
                     return Response(status=status.HTTP_400_BAD_REQUEST)
              if page_number >300:
                     return Response(status=status.HTTP_400_BAD_REQUEST)
             
              return Response(
                     repo.get_car_paginated_results(page_number=page_number),
                     status=status.HTTP_200_OK)

       def post(self,request):
              """Create a new car for rent."""
              repo = Mongo_repository()
              try:
                     validated_data = dict(CarValidator(**request.data))
                     
                     repo.save_carForRent(validated_data)
                     return Response({"status": "success" },status=status.HTTP_201_CREATED)
              
              except ValidationError as e:
                     return Response({"status": "error", "errors": e.errors()}, status=400)
              except DuplicateKeyError:
                     return Response({"status": "error", "message": "Car with this ID already exists"}, status=400)

       def put(self,request):
              """Update an existing car."""
              repo = Mongo_repository()
              try:
                     validated_data = dict(CarValidator(**request.data))
                     repo.edit_car(validated_data)
                     return Response({"status": "success", "updated_car": validated_data})
              
              except ValidationError as e:
                     return Response({"status": "error", "errors": e.errors()}, status=400)

       def delete(self):
              """Delete a car by ID."""
              repo = Mongo_repository()
              car_id = self.request.query_params.get('id', None)
              if not car_id:
                     return Response({"status": "error", "message": "Car ID is required"}, status=400)
              
              repo.delete_car(car_id)
              return Response({"status": "success", "message": "Car deleted successfully"}, status=200)