from django.urls import path
from . import views
from .views import VRegistro

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('logout/', views.salir, name='salir'),
    path('home/', views.home, name='home'),
    path('mis_cursos/', views.pensum, name='allcursos'),
    #path('cursos/', views.CatalogoView, name= 'allcursos'),
    path('cursos_asignados/', views.cursos_asignados, name='cursos_asignados'),
    path('inscribir_curso/<int:curso_id>/', views.inscribir_curso, name='inscribir_curso'),
    path('eliminar_curso/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),
    path('registro/', VRegistro.as_view(), name="registro"),
    path('PortalEstudiantes/', views.PE, name='PE'),
    path('LoginEstudiantes/', views.iniciar_sesion_estudiantes, name='InicioE'),
    path('', views.register, name="register"),
    path('success', views.success, name="success"),
    
    path('InicioS/', views.InicioS, name='InicioS'),
    path('Facial/', views.Facial, name='Facial'),
    
    path('classify/', views.find_user_view, name='classify'), 
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)