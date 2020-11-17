from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class UserList(APIView):
  def get(self,request):
    model=User.objects.all()
    serializers=UsersSerializers(model,many=True)
    return Response(serializers.data)

  def post(self,request):
    serializer=UsersSerializers(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
  def get(self,request,employee_id):
    try:
      model=User.objects.get(id=employee_id)
    except User.DoesNotExist:
      return Response(f"User with {employee_id} is not found in database",status=status.HTTP_404_NOT_FOUND)
    serializers=UsersSerializers(model)
    return Response(serializers.data)

  def put(self,request,employee_id):
    try:
      model=User.objects.get(id=employee_id)
    except User.DoesNotExist:
      return Response(f"User with {employee_id} is not found in database",status=status.HTTP_404_NOT_FOUND)
    serializer=UsersSerializers(model,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,employee_id):
    try:
      model=User.objects.get(id=employee_id)
    except User.DoesNotExist:
      return Response(f"User with {employee_id} is not found in database",status=status.HTTP_404_NOT_FOUND)
    model.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
