from . import views
from django.urls import path

urlpatterns = [
    path('', views.GeoList, name='index'),
    path('table/', views.GeoFull, name='table'),
    path('create/', views.GeoCreate, name='create'),
    path('edit/<id>/', views.GeoEdit, name='edit'),
    path('detail/<id>/', views.GeoDetails, name='detail'),
] 