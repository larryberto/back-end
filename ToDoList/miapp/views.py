from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea

# Create your views here.



def home(request):
    if request.method == 'POST':
        tarea = request.POST.get('tarea')
        descripcion = request.POST.get('descripcion')
        if tarea:
            Tarea.objects.create(tarea=tarea, descripcion=descripcion)
        return redirect('home')
    tareas = Tarea.objects.all().order_by('-fecha_creacion')
    return render(request, 'main.html', {'tareas': tareas})

def eliminar_tarea(request, tarea_id):
    # 1. Obtener la tarea o lanzar un error 404 si no existe
    tarea = get_object_or_404(Tarea, id=tarea_id)

    # 2. Verificar que el método de solicitud sea POST
    if request.method == 'POST':
        # 3. Eliminar la tarea
        tarea.delete()
        
        # 4. Redirigir al usuario (casi siempre a la página principal 'home')
        return redirect('home')

    # Si alguien intenta acceder a esta URL directamente con GET (o si el if falla por alguna razón), redirigir
    return redirect('home')

def cambiar_estado_tarea(request, tarea_id):
    # 1. Busca la tarea. Si no existe, Django lanza un 404.
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    # --- Lógica Crítica ---
    # 2. Invierte el valor booleano: True se convierte en False, y False en True.
    tarea.completada = not tarea.completada
    
    # 3. Guarda el cambio en la base de datos. ¡ESTO ES CRÍTICO!
    tarea.save()
    
    # 4. Redirige a la página principal para ver el cambio.
    return redirect('home')