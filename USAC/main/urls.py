from django.urls import path 
from . import views
from django.conf import settings
from .views import VRegistro
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('carreras/', views.catalogo_de_carreras, name='ingenieria'),
    path('registro/', VRegistro.as_view(), name="registro"),
    
    path('LoginEstudiantes/', views.iniciar_sesion_estudiantes, name="InicioDE"), 
    
    path('LoginDocentes/', views.custom_login, name='IniciarD'),
    path('LoginEstudiantes/', views.iniciar_sesion_estudiantes, name='IniciarE'),
    
    path('PortalEstudiantes/', views.PE, name='PE'),
    
    path('PortalDocentes/', views.PD, name='PD'),
    
   
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)