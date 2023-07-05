from django.urls import path
from . import views

urlpatterns = [
    path('find', views.get_manga, name='get_manga')
]
