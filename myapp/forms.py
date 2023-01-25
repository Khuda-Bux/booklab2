from django import forms
from .models import bloglab

class Mybloglab(forms.ModelForm):

    class Meta:
        model = bloglab
        fields=['title','content','photo']
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
    'content':forms.Textarea(attrs={'class':'form-control'}),
    'photo':forms.ImageField(),
     
    }
    
    