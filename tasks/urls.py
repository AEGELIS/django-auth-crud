from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('singup/', views.singup, name = "singup"),
    path('task/', views.tasks, name = "task"),
    path('task_complete/', views.tasks_completed, name = "tasks_completed"),
    path('singout/', views.singout, name = "singout"),
    path('singin/', views.singin, name = "singin"),
    path('create_task/', views.create_task, name = "create_task"),
    path('task_detail/<int:task_id>/', views.task_detail, name = "task_detail"),
    path('task_detail/<int:task_id>/complete', views.complete_task, name = "complete_task"),
    path('task_detail/<int:task_id>/delete', views.delete_task, name = "delete"),
]