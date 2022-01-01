from django.urls import path

from . import views
from . import fyers

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('logout', views.logout),
    path('register', views.register),

    path('generateAuthCode', fyers.generateAuthCode),
    path('generateToken/<str:s>/<str:code>/<str:auth_code>/', fyers.generateToken),
    
    
    
]