import imp
from . import views
from django.urls import path
from geo.views import CustomLoginView
from geo.forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.GeoList, name='index'),
    path('table/', views.GeoFull, name='table'),
    path('create/', views.GeoCreate, name='create'),
    path('edit/<id>/', views.GeoEdit, name='edit'),
    path('detail/<id>/', views.GeoDetails, name='detail'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, 
                                            template_name='login.html', 
                                            authentication_form=LoginForm), 
                                            name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

] 