from django.contrib import admin

# Register your models here.
from .models import Cliente, Producto

admin.site.register(Cliente)
admin.site.register(Producto)