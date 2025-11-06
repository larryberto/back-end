from django.shortcuts import render
from .models import Tarea
from .forms import TareaForm
# Create your views here.



def home(request):
    if request.method == 'POST':
        form =TareaForm(request.POST)
        if form.is_valid():
            form.save()
            
    form = TareaForm()
    tareas = Tarea.objects.all()
    context = {'tareas': tareas, 'form': form}
    return render(request, 'main.html', context)

