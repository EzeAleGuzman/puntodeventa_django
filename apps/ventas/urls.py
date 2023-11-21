from django.urls import path
from . import views


urlpatterns = [
    path('',views.ventas_view, name='ventas'),
    path('clientes/',views.clientes_view, name='clientes'),
    path('add_cliente/', views.add_clientes_view, name ='add_cliente'),
    path('edit_cliente/', views.edit_clientes_view, name ='edit_cliente'),
    path("delete/", views.delete_clientes_view, name="delete_cliente"),
]