from django.contrib import admin
from .models import Profesional, Rol, Cliente
# Register your models here.

admin.site.register(Rol)
admin.site.register(Cliente)
admin.site.register(Profesional)