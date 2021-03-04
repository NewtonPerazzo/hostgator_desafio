from django import forms
from app.models import Dominio


class DominioForm(forms.ModelForm):
    class Meta():
        model = Dominio
        fields = ['dominio']