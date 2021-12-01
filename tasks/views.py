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


@api_view(['GET', 'POST'])
def task_detail(request):

    if request.method == 'GET':
        all_tasks = Task.objects.all()
        serializer_json = serializers.serialize("json", all_tasks)
        return HttpResponse(serializer_json, content_type="application/json", status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['GET'])
def get_task(request):
    all_tasks = Task.objects.all()
    serializer_json = serializers.serialize("json", all_tasks)
    return HttpResponse(serializer_json, content_type="application/json")

@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    task.delete()
    return JsonResponse({"message": "Task deletada com sucesso"}, status=status.HTTP_200_OK)
