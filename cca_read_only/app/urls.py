from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('get-names', views.get_names, name="get-names")
]
