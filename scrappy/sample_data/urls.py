from django.urls import path
from . import views

urlpatterns = [
    path('artists', views.get_data, name='get_data'),
    path('wait', views.wait_for_me, name="wait_for_me"),
    path('sleep', views.sleep_task, name='sleep_task'),
    path('check', views.get_task_status, name='get_task_status')
]
