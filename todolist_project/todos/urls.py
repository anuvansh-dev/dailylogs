from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('/add', views.add_task, name='add_task'),
    path('/task/<int:task_id>', views.task_detail, name='task_detail'),
    path('/task/edit/<int:task_id>', views.task_edit, name='task_edit'),
    path('/task/delete/<int:task_id>', views.task_delete, name='task_delete'),
]