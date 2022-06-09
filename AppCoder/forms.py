from unittest.util import _MAX_LENGTH
from django import forms


class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class Profesores_formulario(forms.Form):
  nombre = forms.CharField(max_length=30)
  apellido = forms.CharField(max_length=30)
  email = forms.EmailField(max_length=30)
  profesion = forms.CharField(max_length=30)


class Estudiantes_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)