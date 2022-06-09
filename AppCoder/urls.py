from django.urls import path

from AppCoder import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores_formulario, name="Profesores"),
    path('estudiantes', views.estudiantes_formulario, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar)
]

