from django import forms
from . import models

#Creation of form with the title field
class CreateStoreItem(forms.ModelForm):
    class Meta:
        model = models.Storemodel
        fields = ['title']
