from django.shortcuts import render, redirect, get_object_or_404
from .forms import contactoform, productoform, CustomUserForm
from .models import producto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def cuenta(request):
    return render(request, 'app/cuenta.html')

@login_required
def api(request):
    return render(request, 'app/api.html')

@login_required
def carrito(request):
    return render(request, 'app/carrito.html')

def inicio(request):
    return render(request, 'app/inicio.html')

@login_required
def objetos(request):
    productos = producto.objects.all()
    data = {
        'productos': producto
    }
    return render(request, 'app/objetos.html', data)

def recuperar(request):
    return render(request, 'app/recuperar.html')

@login_required
def soporte(request):
    data = {
        'form': contactoform()
    }
    
    if request.method == 'POST':
        formulario = contactoform(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = 'formulario enviado'
        else:
            data["form"] = formulario
    return render(request, 'app/soporte.html', data)

def souls(request):
    return render(request, 'app/souls.html')


def agregar_producto(request):
    data = {
        'form': productoform()
    }

    if request.method == 'POST':
        formulario = productoform(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = 'guardado correctamente'
        else:
            data["form"] = formulario
    return render(request,'app/CRUD/agregar.html', data )

def listar_productos(request):
    productos = producto.objects.all()
    data ={
        'productos': productos
    }
    return render(request,'app/CRUD/listar.html')

def modificar_productos(request, id):
    
    producto = get_object_or_404(producto, id=id)

    data ={
        'form': productoform(instance=producto)
    }

    return render(request, 'app/CRUD/modificar.html', data)

def registrar_usuario(request):
    data ={
        'form': CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #autentificar al usuario y redirigirlo al inicio
            username = formulario.cleaned_data('username')
            password = formulario.cleaned_data('contraseña')
            user = authenticate(username='userame', password='password')
            login(request, user)
            return redirect(to='index')
        else:
            data["form"] = formulario
    return render(request,'registration/registrar.html', data)
