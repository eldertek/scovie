from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('screen/all/', views.all, name='all'),
    path('screen/informations/', views.informations, name='informations'),
    path('screen/caroussel/', views.caroussel, name='caroussel'),
    path('screen/events/valentine', views.valentine, name='valentine')
]
