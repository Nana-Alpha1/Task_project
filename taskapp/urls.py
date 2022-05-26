from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='taskapp-index'),
    path('about/',views.about, name='taskapp-about'),
    path('delete/<int:pk>/',views.delete, name='taskapp-delete'),
    path('edit/<int:pk>/',views.edit, name='taskapp-edit')
]