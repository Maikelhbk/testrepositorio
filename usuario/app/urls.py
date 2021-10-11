from django.urls import path
from .views import home, cliente


urlpatterns = [
    path('', home, name="home"),
    path('cliente/', cliente, name="cliente"),
]
