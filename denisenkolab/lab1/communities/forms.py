from django import forms 
from . import models 

class CreateCommunity(forms.ModelForm): 
    class Meta: 
        model = models.Community
        fields = ['name','description','slug','banner','free']