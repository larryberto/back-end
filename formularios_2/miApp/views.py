from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm
# 
#def home(request):
    #context = {}
    #if request.method == "POST":
        # Obtenemos los datos
     #   nombre_u = request.POST.get('nombre_u')
    #    apellido_u = request.POST.get('apellido_u')
        # Crear un objeto Persona
   #     p = Persona(nombre=nombre_u,apellido=apellido_u)
  #      p.save()
 #   context['personas'] = Persona.objects.all()
#    return render(request,"main.html",context)




#ef home(request):
#    context = {}
 #   form = PersonaForm()
  #  if request.method == "POST":
   #     pass
    
    #context['form'] = form
    #context['personas'] = Persona.objects.all()
    #return render(request,"main.html",context)





#def home(request):
#    context = {}
 #   if request.method == "POST":
  #      form = PersonaForm(request.POST)
   #     if form.is_valid():
    #        
     #       nombre_limpio = form.cleaned_data['nombre']
      #      apellido_limpio = form.cleaned_data['apellido']
       #     
        #    p = Persona(nombre = nombre_limpio, apellido = apellido_limpio)
         #   p.save
 #       else:
  #          context['errores'] = form.errors
   #         
   # form = PersonaForm()
    #context['form'] = form
    #context['personas'] = Persona.objects.all()
    #return render(request,"main.html",context)
    
    
    
    
    
def home(request):
    context = {}
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
           form.save()
           
        else:
            context['errors'] = form.errors
    
            
    form = PersonaForm()
    context['form'] = form
    context['personas'] = Persona.objects.all()
    return render(request,"main.html",context)
    
    
    
    
    
    
    

    
    
    