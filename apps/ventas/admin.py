from django.contrib import admin
from apps.ventas.models import Cliente, Producto

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre', 'telefono')
    search_fields =['nombre']
    readonly_fields = ('created', 'update')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Cliente, ClienteAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre', 'costo', 'cantidad','descripcion')
    search_fields =['nombre']
    readonly_fields = ('created', 'update')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Producto, ProductoAdmin)