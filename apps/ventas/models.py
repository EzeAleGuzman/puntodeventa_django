from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    codigo = models.IntegerField(null=False, unique=True, blank=False)
    nombre = models.CharField( max_length=50)
    telefono = models.CharField(max_length=50,)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    
    class meta:
        verbose_name ="cliente"
        verbose_name_plural = 'clientes'
        
    def __str__(self):
        return f'Codigo: {self.codigo} Cliente:  {self.nombre.upper()}'
    


class Producto(models.Model):
    codigo = models.IntegerField(null=False, unique=True, blank=False)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to= 'productos',null=True , blank= True)
    descripcion = models.CharField(max_length=50, null=False)
    costo = models.DecimalField(max_digits=15, decimal_places=2, null= False)
    cantidad = models.DecimalField(max_digits=15, decimal_places=2, null= False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    
    class meta:
        verbose_name="producto"
        verbose_name_plural = 'productos'
        order_with_respect_to = 'codigo'
        
    def __str__(self):
        return f'{self.nombre} {self.codigo}'
    

