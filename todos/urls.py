from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_todo_items),
    path('insert_todo/', views.insert_todo_item, name='insert_todo'),
    path('delete_todo/<int:id>/', views.delete_todo_item, name='delete_todo'), 
]