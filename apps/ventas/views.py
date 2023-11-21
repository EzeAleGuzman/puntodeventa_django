from django.shortcuts import render, redirect
from .models import Cliente, Producto



def ventas_view(request):
    return render(request, 'ventas.html')

def clientes_view(request):
    clientes = Cliente.objects.all()
    context = {
     'clientes' : clientes
    }
    return render(request, 'clientes.html',context)

def add_clientes_view(redirect):
    clientes = Cliente.objects.all()
    context = {
        'clientes' : clientes
    }
    
    return redirect('clientes')

def edit_clientes_view(redirect):
    clientes = Cliente.objects.all()
    context = {
        'clientes' : clientes
    }
    return redirect('clientes')

def delete_clientes_view(redirect):
    clientes = Cliente.objects.all()
    context = {
        'clientes' : clientes
    }
    
    return redirect('clientes', context)