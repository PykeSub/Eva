from django import forms
from distribuidorApp.models import Distribuidor

class formDistribuidor(forms.ModelForm):
    class Meta:
        model = Distribuidor
        fields = '__all__'