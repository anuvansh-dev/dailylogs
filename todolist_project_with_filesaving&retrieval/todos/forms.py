from django import forms
from .models import Tasks
from .models import BackgroundImage

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'is_completed']
        
class BackgroundImageForm(forms.ModelForm):
    class Meta:
        model = BackgroundImage
        fields = ['image']