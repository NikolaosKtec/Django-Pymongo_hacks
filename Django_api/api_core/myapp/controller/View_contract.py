from pydantic_core import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..model.Models import ContractModel
from ..db.Contract_repository import Contract_repository
from pymongo.errors import DuplicateKeyError
from bson import ObjectId
class View_contract(APIView):
       def get(self,request,*args, **kwargs):
              """Retrieve paginated results of contracts.
              This endpoint allows you to retrieve a paginated list of contracts."""
              try:
                     repo = Contract_repository()
                     page = int(request.query_params.get('page'))
                     if page <= 0:
                            return Response(status=status.HTTP_400_BAD_REQUEST)
                     if page >300:
                            return Response(status=status.HTTP_400_BAD_REQUEST)
              except Exception as e:
                     return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
             
              return Response(
                     repo.get_contract_paginated_results(page=page),
                     status=status.HTTP_200_OK)

       def post(self,request):
              """Create a new contract.
              This endpoint allows you to create a new contract by providing the necessary details."""
              repo = Contract_repository()
              try:
                     validated_data = ContractModel(**request.data)
                     repo.save(validated_data)
                     return Response({"status": "success"}, status=201)
              
              except ValidationError as e:
                     return Response({"status": "error", "errors": e.errors()}, status=400)
              except DuplicateKeyError:
                     return Response({"status": "error", "message": "Contract with this ID already exists"}, status=400)
              # except Exception as e:
              #        return Response({"status": "error", "message": str(e)}, status=400)
       def put(self,request):
              """Update an existing contract.
              """
              repo = Contract_repository()
              try:
                     validated_data = ContractModel(**request.data)
                     repo.update_one({"id": validated_data['id']}, {"$set": validated_data})
                     return Response({"status": "success", "updated_contract": validated_data})
              
              except ValidationError as e:
                     return Response({"status": "error", "errors": e.errors()}, status=400)
              except Exception as e:
                     return Response({"status": "error", "message": str(e)}, status=400)

       def delete(self):
              repo = Contract_repository()
              contract_id = self.request.query_params.get('id', None)
              if not contract_id:
                     return Response({"status": "error", "message": "Contract ID is required"}, status=400)
              
              if not repo.find_one_by_id(ObjectId(contract_id)):
                     return Response({"status": "error", "message": "Contract not found"}, status=404)
              repo.delete_by_id(ObjectId(contract_id))
              return Response({"status": "success", "message": "Contract deleted successfully"}, status=200)
              
