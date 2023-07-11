from django.db import models

# Create your models here.
class Usuario(models.Model):
    
    username = models.CharField(max_length=15)
    correo = models.EmailField(blank=False, null=False)
    Contraseña  = models.CharField(max_length= 20, blank= False, null= False)

    def __str__(self):
        return self.username

class Suscripcion(models.Model):
    activo = models.BooleanField(Usuario)
    FechaSus = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activo

opciones_consultas = [
    [0, "consultas"],
    [1,"reclamo"],
    [2,"sugerencia"]
]    
    
class contacto(models.Model):
    username = models.CharField(max_length=15)
    correo = models.EmailField(blank=False, null=False)
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.username

    

class producto(models.Model):
    nombre = models.CharField(max_length=15)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

