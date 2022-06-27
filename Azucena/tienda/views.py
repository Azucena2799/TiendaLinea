from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect


from tienda.models import Producto,Cliente
from tienda.modelForms import ProductoForm, ClienteForm

# Create your views here.

def Tienda(request, id):    
    c = Cliente.objects.get(pk=id)
    p = Producto.objects.all()
    context = {
        'productos': p
    }
    
    return render(request,'tienda/Tienda.html',context)


def Clientes(request):
    c = Cliente.objects.all()
    context = {
        'clientes': c
    }
    
    return render(request,'tienda/Clientes.html',context)
def AgregarCliente(request):
    if request.method == 'POST':
        formr = ClienteForm(request.POST)
        if formr.is_valid():
            formr.save()          
            return Clientes(request)
    else:
        formset = ClienteForm()
    return render(request,'tienda/AgregarCliente.html',{'miform': formset})
def deleteC(request, idc):
    try:
       r1 = Cliente.objects.get(id=idc)
       r1.delete()
       return Clientes(request)
    except:
       print('')
       return Clientes(request)
def showEdit(request, ide): 
    r = Cliente.objects.get(id=ide)
    if request.method == 'GET':
        formulario = ClienteForm(instance=r)
        return render(request,'tienda/editar.html',{'form': formulario})

    elif request.method == 'POST':
        formulario = ClienteForm(request.POST,intance=r)
        if formulario.is_valid():
            formulario.save()
        return Clientes(request)

def Plantas(request):
    p = Producto.objects.all()
    context = {
        'productos': p
    }
    return render(request,'tienda/Plantas.html',context)

def AgregarPlanta(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario .is_valid():
            formulario .save()          
            return Plantas(request)
    else:
        formulario  = ProductoForm()
    return render(request,'tienda/AgregarPlanta.html',{'formulario': formulario })

def deletep(request, idr):
    try:
       r1 = Producto.objects.get(id=idr)
       r1.delete()
       return Plantas(request)
    except:
       print('')
       return Plantas(request)

