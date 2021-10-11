from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add-name', views.add_name, name="add-name"),
]
