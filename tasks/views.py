from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.core import serializers




# Create your views here.

# class TaskViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


@api_view(['GET', 'POST', 'DELETE'])
def task_detail(request, pk):
    """
    Retrieve, update or delete a code task.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # serializer = TaskSerializer(all_tasks)
        all_tasks = Task.objects.all()
        serializer_json = serializers.serialize("json", all_tasks)
        return HttpResponse(serializer_json, content_type="application/json")

    elif request.method == 'POST':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_task(request):
    all_tasks = Task.objects.all()
    serializer_json = serializers.serialize("json", all_tasks)
    return HttpResponse(serializer_json, content_type="application/json")