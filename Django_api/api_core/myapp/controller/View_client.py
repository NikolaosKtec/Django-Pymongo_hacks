from pydantic_core import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..data.DataFormAbstract import ClientValidator
from ..db.Mongo_repository import Mongo_repository
from pymongo.errors import DuplicateKeyError

class View_client(APIView):
       def get(self,request,page_number=1,*args, **kwargs):
              """Retrieve paginated results of clients.
              This endpoint allows you to retrieve a paginated list of clients."""
              repo = Mongo_repository()

              if page_number <= 0:
                     return Response(status=status.HTTP_400_BAD_REQUEST)
              if page_number >300:
                     return Response(status=status.HTTP_400_BAD_REQUEST)
             
              return Response(
                     repo.get_client_paginated_results(page_number=page_number),
                     status=status.HTTP_200_OK)

       def post(self,request):
              """Create a new client.
              This endpoint allows you to create a new client by providing the necessary details."""
              repo = Mongo_repository()
              try:
                     validated_data = dict(ClientValidator(**request.data))
                     
                     repo.save_client(validated_data)
                     
                     return Response({"status": "success"}, status=201)
              
              except ValidationError as e:
                     return Response({"status": "error", "errors": e.errors()}, status=400)
              except DuplicateKeyError:
                     return Response({"status": "error", "message": "Client with this ID already exists"}, status=400)

       def put(self,request):
              repo = Mongo_repository()
              try:
                     validated_data = dict(ClientValidator(**request.data))
                     repo.edit_client(validated_data)
                     return Response({"status": "success", "updated_client": validated_data})
              
              except ValidationError as e:
                     return Response({"status": "error", "errors": e.errors()}, status=400)

       def delete(self,request):
              repo = Mongo_repository()
              client_id = self.request.query_params.get('id', None)
              if not client_id:
                     return Response({"status": "error", "message": "Client ID is required"}, status=400)
              
              repo.delete_client(client_id)
              return Response({"status": "success", "message": "Client deleted successfully"}, status=200)
