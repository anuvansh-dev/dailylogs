from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),  # Remove the leading slash
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),  # Remove the leading slash
    path('task/edit/<int:task_id>/', views.task_edit, name='task_edit'),  # Remove the leading slash
    path('task/delete/<int:task_id>/', views.task_delete, name='task_delete'),  # Remove the leading slash
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('upload-background', views.upload_background, name='upload_background'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)