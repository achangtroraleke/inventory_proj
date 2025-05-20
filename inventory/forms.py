# forms.py
from django import forms
from .models import Container

class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ['name']
        # By default, CharField is required, ensuring the name is provided.
