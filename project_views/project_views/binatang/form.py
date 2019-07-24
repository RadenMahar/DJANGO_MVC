from django import forms
from .models import Binatang

class InputBinatang(forms.ModelForm):

    class Meta:
        model = Binatang
        fields = ('nama', 'jenis', 'umur')