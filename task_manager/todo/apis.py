from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from .serializers import ListSerializer
from .models import  List


class ListUpdateAPI(generics.UpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        task = List.objects.get(
            user=request.user,
            name = kwargs["name"],
        )
        print(task)
        task.name = request.data["name"]
        task.weight = request.data["weight"]
        task.save()

        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Task Updated Successfully',
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)
