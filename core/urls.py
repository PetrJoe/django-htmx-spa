from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('landingpage/', landingpage, name='landingpage'),
    path('about/', about, name='about'),
]
