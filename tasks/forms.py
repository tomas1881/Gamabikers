from django import forms
from .models import Post
from django.db import models


class VentaForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Nombre_vendedor', 'marca', 'año', 'descripcion', 'foto']