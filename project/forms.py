from django import forms
from .models import Empleado, Clientes, Producto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre', 'apellido', 'email']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'valor']

class BuscarForm(forms.Form):
    valor = forms.CharField(label="Valor a buscar", max_length=200)
