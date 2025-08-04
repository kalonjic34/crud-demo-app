
from django.forms import ModelForm
from . models import Task

class TaskForm(ModelForm):
    class Metal:
        model = Task
        fields = '__all__'
        
    
        