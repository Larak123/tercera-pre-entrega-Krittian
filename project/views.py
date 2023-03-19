
from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes, Empleado, Producto
from .forms import ClienteForm, EmpleadoForm, ProductoForm, BuscarForm


# Create your views here.

def editar_empleados(request, empleado_id):
    if request.method == 'GET':
        empleado = get_object_or_404(Empleado, pk=empleado_id)
        formulario = EmpleadoForm(instance=empleado)
        return render(request, 'AppK/editar_empleado.html', {'empleado': empleado, 'formulario': formulario})
    else:
        try:
            empleado = get_object_or_404(Empleado, pk=empleado_id)
            formulario = EmpleadoForm(request.POST, instance=empleado)
            formulario.save()
            return redirect('empleados')
        except ValueError:
            return render(request, 'AppK/editar_empleado.html', {'empleado': empleado, 'formulario': formulario, 'error': 'error'})

def borrar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleados')

def buscar(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            clientes = list(Clientes.objects.values())
            # Se comprueba si el valor es un cliente
            for cliente in clientes:
                if form.cleaned_data['valor'] == cliente['nombre'] or form.cleaned_data['valor'] == cliente['apellido']:
                    result = cliente['nombre'] + ' ' + cliente['apellido']

                    return render(request, 'AppK/buscar.html', {'form': form, 'value': result + " es un cliente"})
                else:
                    # Se comprueba si el valor es un empleado
                    empleados = list(Empleado.objects.values())
                    for empleado in empleados:
                        if form.cleaned_data['valor'] == empleado['nombre'] or form.cleaned_data['valor'] == empleado[
                            'apellido']:
                            result = empleado['nombre'] + ' ' + empleado['apellido']

                            return render(request, 'AppK/buscar.html', {'form': form, 'value': result + " es un empleado"})
                        else:
                            # Se comprueba si el valor es un producto
                            productos = list(Producto.objects.values())
                            for producto in productos:
                                if form.cleaned_data['valor'] == producto['nombre']:
                                    result = producto['nombre']

                                    return render(request, 'AppK/buscar.html',
                                                  {'form': form, 'value': result + " es un producto"})

                    else:
                        return render(request, 'AppK/buscar.html', {'form': form, 'value': 'No se encontro el valor buscado'})

    else:
        form = BuscarForm()

    return render(request, 'AppK/buscar.html', {'form': form})


def clientes(request):

    clientes = Clientes.objects.all()
    return render(request, 'AppK/clientes.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == "POST":
        mi_formulario = ClienteForm(request.POST)
        if mi_formulario.is_valid():
            Clientes.objects.create(
                nombre=mi_formulario.cleaned_data["nombre"],
                apellido=mi_formulario.cleaned_data["apellido"],
                email=mi_formulario.cleaned_data["email"]
            )

            return redirect('clientes')
    else:
        mi_formulario = ClienteForm()

    return render(request, 'AppK/crear_clientes.html', {'form_clientes': mi_formulario})

def editar_clientes(request, cliente_id):
    if request.method == 'GET':
        cliente = get_object_or_404(Clientes, pk=cliente_id)
        formulario = ClienteForm(instance=cliente)
        return render(request, 'AppK/editar_cliente.html', {'cliente': cliente, 'formulario': formulario})
    else:
        try:
            cliente = get_object_or_404(Clientes, pk=cliente_id)
            formulario = ClienteForm(request.POST, instance=cliente)
            formulario.save()
            return redirect('clientes')
        except ValueError:
            return render(request, 'AppK/editar_cliente.html', {'cliente': cliente, 'formulario': formulario, 'error': 'error'})

def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Clientes, pk=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')

def empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'AppK/empleado.html', {'empleados': empleados})

def crear_empleado(request):
    if request.method == "POST":
        mi_formulario = EmpleadoForm(request.POST)
        if mi_formulario.is_valid():
            Empleado.objects.create(
                nombre=mi_formulario.cleaned_data["nombre"],
                apellido=mi_formulario.cleaned_data["apellido"]
            )

            return redirect('empleados')
    else:
        mi_formulario = EmpleadoForm()

    return render(request, 'AppK/crear_empleado.html', {'form_empleados': mi_formulario})

def productos(request):
    productos = list(Producto.objects.values())
    productos = Producto.objects.all()
    return render(request, 'AppK/producto.html', {'productos': productos})

def crear_producto(request):
    if request.method == "POST":
        mi_formulario = ProductoForm(request.POST)
        if mi_formulario.is_valid():
            Producto.objects.create(
                nombre=mi_formulario.cleaned_data["nombre"],
                valor=mi_formulario.cleaned_data["valor"]
            )

            return redirect('productos')
    else:
        mi_formulario = ProductoForm()

    return render(request, 'AppK/crear_producto.html', {'form_productos': mi_formulario})

def editar_productos(request, producto_id):
    if request.method == 'GET':
        producto = get_object_or_404(Producto, pk=producto_id)
        formulario = ProductoForm(instance=producto)
        return render(request, 'AppK/editar_producto.html', {'producto': producto, 'formulario': formulario})
    else:
        try:
            producto = get_object_or_404(Producto, pk=producto_id)
            formulario = ProductoForm(request.POST, instance=producto)
            formulario.save()
            return redirect('productos')
        except ValueError:
            return render(request, 'AppK/editar_producto.html', {'producto': producto, 'formulario': formulario, 'error': 'error'})

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')

def index (request):
    return render(request, "base.html")


