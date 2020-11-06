from django import forms
from .models import rating, thumbnail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

MAX_RATE = 10

LANGUAGE_DROPDOWN = (
    ('Tamil', 'TAMIL'),
    ('English', 'ENGLISH'),
    ('Telugu', 'TELUGU'),
    ('Hindi', 'HINDI'),
    ('Malayalam', 'MALAYALAM'),
    ('Urdhu', 'URDHU')
)

class input_form(forms.ModelForm):
    class Meta:
        model = rating
        fields = ["rate"]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
class new_movie_form(forms.ModelForm):
    class Meta:
        model = thumbnail
        fields = ['title', 'image', 'content', 'genre', 'language']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','rows':1.5, 'cols':40}),
            'content' : forms.Textarea(attrs={'class':'form-control' ,'rows':3, 'cols':40}),
            'language' : forms.Select(attrs={'class':'form-control'}),
            'genre' : forms.Select(attrs={'class':'form-control'}),
            #'avg_rate' : forms.Textarea(attrs={'rows':1.5, 'cols':40}),
        }