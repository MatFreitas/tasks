from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/<int:pk>', views.task_detail, name='tasks'),
    path('allTasks/', views.get_task, name='allTasks'),
    path('postTasks/', views.post_task, name='postTasks'),
]
