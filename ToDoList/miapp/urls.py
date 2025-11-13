from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('eliminar_tarea/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('estado/<int:tarea_id>/', views.cambiar_estado_tarea, name='cambiar_estado'),
]
