from django.urls import path
from CusquiApp.vistas.home import *
from CusquiApp.vistas.inicioSesion import *
from CusquiApp.vistas.registro import *
from CusquiApp.vistas.proveedores import *
from CusquiApp.vistas.vistaG import *
from CusquiApp.vistas.perfil import *

urlpatterns = [
    path('home/', home),
    path('inicioS/', inicioS),
    path('registro/', registro),
    path('proveedores/', proveedores),
    path('vistaG/', vistaG),
    path('perfil/', perfil),
    path('añadir/', añadir),
    path('nuevoPro/', nuevoPro),

]
