from django import forms
from .models import thumbnail

class input_form(forms.ModelForm):
    class Meta:
        model = thumbnail
        fields = ['content']
