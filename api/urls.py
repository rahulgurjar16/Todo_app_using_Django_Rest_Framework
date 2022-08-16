from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_overview, name="api_overview"),
    path('task-detail/<str:pk>', views.taskdetail, name='task-detail'),
    path('task-list/', views.tasklist, name='tasklist'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>', views.taskDelete, name='task-delete'),
]
