from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('crear_clientes/', views.crear_cliente, name="crear_cliente"),
    path('clientes/', views.clientes, name="clientes"),
    path('crear_empleado/', views.crear_empleado, name="crear_empleado"),
    path('clientes/<int:cliente_id>/', views.editar_clientes, name='editar_clientes'),
    path('clientes/<int:cliente_id>/borrar', views.borrar_cliente, name='borrar_clientes'),
    path('empleados/', views.empleados, name="empleados"),
    path('empleados/<int:empleado_id>/', views.editar_empleados, name='editar_empleados'),
    path('empleados/<int:empleado_id>/borrar', views.borrar_empleado, name='borrar_empleado'),
    path('crear_producto/', views.crear_producto, name="crear_producto"),
    path('productos/', views.productos, name="productos"),
    path('productos/<int:producto_id>/', views.editar_productos, name='editar_productos'),
    path('productos/<int:producto_id>/borrar', views.borrar_producto, name='borrar_producto'),
    path('buscar/', views.buscar, name="buscar")

    #path('empleados/<int:empleado_id>/eliminar', views.eliminar_empleados, name='eliminar_empleados'),


]