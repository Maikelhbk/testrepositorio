from django.urls import path
from .views import home, cliente, menu_cliente, menu_profesional, profesional, registro, modificar_cliente


urlpatterns = [
    path('', home, name="home"),
    path('cliente/', cliente, name="cliente"),
    path('profesional/', profesional, name="profesional"),
    path('registro/', registro, name="registro"),
    path('menu_cliente/',menu_cliente,name="menu_cliente"),
    path('menu_profesional/', menu_profesional, name="menu_profesional"),
    path('modificar-cliente/<id>/', modificar_cliente, name="modificar_cliente")
]
