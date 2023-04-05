from django.urls import path
from . import views

urlpatterns = [
    path('artists', views.get_data, name='get_data'),
]
