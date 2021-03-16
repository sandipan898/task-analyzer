from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import List
from .serializers import ListSerializer


class TaskUpdateAPI(generics.GenericAPIView):
    """ Save a Product with the Informations provided """
    
    serializer_class = ListSerializer
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        task = List.objects.get(
            id = kwargs["id"],
        )
        print(task)
        task.name = request.data['name']
        task.weight = request.data['weight']
        task.save()

        response = {
            "success": True,
            "message": "Task Updated Successfully",
            "status code": status.HTTP_200_OK,
        }
        return Response(response)
