from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.AddItem, name='newitem'),
    path('delete/<int:todo_id>', views.DeleteItem, name='deleteitem'),
]
