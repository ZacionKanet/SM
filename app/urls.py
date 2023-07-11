from django.urls import path
from .views import index, cuenta, carrito, api, inicio, objetos, recuperar, soporte, souls, agregar_producto, listar_productos, modificar_productos, registrar_usuario

urlpatterns = [
    path('', index, name="index"),
    path('cuenta/', cuenta, name="cuenta"),
    path('carrito/', carrito, name="carrito"),
    path('api/', api, name="api"),
    path('inicio/', inicio, name="inicio"),
    path('objetos/', objetos, name="objetos"),
    path('recuperar/', recuperar, name="recuperar"),
    path('soporte/', soporte, name="soporte"),
    path('souls/', souls, name="souls"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/',listar_productos, name="lista_productos"),
    path('modificar-productos/<id>/',modificar_productos, name="modificar_productos"),
    path('registrar/', registrar_usuario,name="registrar_usuario")
    

]