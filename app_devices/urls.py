from django.urls import path
# from .views import car_list, add_car
from . import views

urlpatterns = [
    # path('', views.car_list, name='car_list'),
    path('', views.add_car, name='add_car'),
]
