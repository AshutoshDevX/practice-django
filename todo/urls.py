from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
    path('',views.task_list, name='task_list'),
    path('add/',views.task_create, name='add'),
    path('edit/<int:pk>/',views.task_update,name='task_update'),
    path('delete/<int:pk>/',views.task_toggle_complete,name='task_toggle_complete'),
]