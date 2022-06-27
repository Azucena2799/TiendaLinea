from django.urls import path
from . import views
app_name = 'tienda'





urlpatterns = [
    path('Clientes/',views.Clientes, name ='Clientes'),
    path('AgregarCliente/>',views.AgregarCliente, name ='AgregarCliente'),
    path('deleteC/<int:idc>',views.deleteC,name="deleteC"),
    path('showEdit/<int:ide>',views.showEdit, name ='showEdit'),

    path('Plantas/',views.Plantas, name ='Plantas'),
    path('AgregarPlanta/>',views.AgregarPlanta, name ='AgregarPlanta'),
    path('deletep/<int:idr>',views.deletep,name="deletep"),
    
    path('Tienda/<int:id>',views.Tienda, name ='Tienda'),
    
]
