from django import forms
from .models import Persona

#class PersonaForm(forms.Form):
    # definir imputs 
 #   nombre = forms.CharField(max_length=50)
  #  apellido = forms.CharField(max_length=200)
    
    
   # def clean_nombre(self):
#       if len(nombre) > 8:
 #       raise forms.ValidationError("nombre no puede ser mas largo que 8 caracteres")
  #      return nombre
  
  
  
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
       # fields = ['nombre','apellido']
        fields = '__all__'