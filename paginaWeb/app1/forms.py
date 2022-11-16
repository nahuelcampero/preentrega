from django import forms

    
class cineForm(forms.Form):
    nombre = forms.CharField(max_length = 40)
    direccion = forms.CharField(max_length = 40)
    
class peliculaForm(forms.Form):

    nombre = forms.CharField(max_length = 40)
    duracion = forms.IntegerField()


class clienteForm(forms.Form):
    nombre = forms.CharField(max_length = 40)
    apellido = forms.CharField(max_length = 40)
    DNI = forms.IntegerField()
    
    