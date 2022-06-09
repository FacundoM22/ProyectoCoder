from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Profesor
from AppCoder.forms import Curso_formulario , Profesores_formulario , Estudiantes_formulario


# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")

def cursos(request):

      return render(request, "AppCoder/cursos.html")

def profesores(request):

      return render(request, "AppCoder/profesores.html")


def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def curso_formulario(request):
      if request.method == "POST":
       mi_formulario = Curso_formulario(request.POST)

       if mi_formulario.is_valid():
             print(mi_formulario.cleaned_data)
       curso = Curso(nombre=request.POST['nombre'], camada=request.POST['camada'])
       curso.save()
       return render(request, "AppCoder/cursos.html")

      return render(request, "AppCoder/cursos.html")

 
def profesores_formulario(request):
     if request.method == "POST":
       mi_formulario = Profesores_formulario(request.POST)

       if mi_formulario.is_valid():
             print(mi_formulario.cleaned_data)
       profesor = Profesor(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'], profesion=request.POST['profesion'])
       profesor.save()
       return render(request, "AppCoder/profesores.html")

     return render(request, "AppCoder/profesores.html")


   
def estudiantes_formulario(request):
      if request.method == "POST":
       mi_formulario = Estudiantes_formulario(request.POST)

       if mi_formulario.is_valid():
             print(mi_formulario.cleaned_data)
       estudiantes = Estudiante(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'])
       estudiantes.save()
       return render(request, "AppCoder/estudiantes.html")

      return render(request, "AppCoder/estudiantes.html")

      


def buscar_curso(request):
      return render( request, "AppCoder/buscar_curso.html")



def entregables(request):

      return render(request, "AppCoder/entregables.html")


def buscar(request):
       if request.GET['nombre']:
             nombre = request.GET['nombre']
             cursos = Curso.objects.filter(nombre__icontains = nombre)
             return render (request , "AppCoder/resultado_busqueda.html", {"cursos": cursos})
             
       else:
             return HttpResponse("campo vacio")

      