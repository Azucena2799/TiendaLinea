from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()

    imagen = models.ImageField(upload_to='images/')
    def __str__(self):
        return "ID: [{0}], Titulo: {1}, Precio: {2}".format(self.id,self.nombre,self.precio)

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    dinero = models.FloatField()
    contraseña = models.CharField(max_length=10)
    total = models.FloatField(default=0)
    correo = models.EmailField()
    clientes = models.ManyToManyField(Producto)
    def __str__(self):
        return "ID: [{0}], Nombre: {1}, Dinero: {2}".format(self.id,self.nombre,self.dinero)
