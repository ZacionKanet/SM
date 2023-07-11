from django.contrib import admin
from .models import Usuario, Suscripcion, contacto, producto


# Register your models here.
admin.site.register(Usuario)
admin.site.register(Suscripcion)
admin.site.register(contacto)
admin.site.register(producto)