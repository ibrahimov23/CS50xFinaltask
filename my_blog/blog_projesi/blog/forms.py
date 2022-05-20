from django import forms
from . import models

class AddParfumeForm(forms.ModelForm):
    class Meta:
        model = models.Parfume
        fields = '__all__'