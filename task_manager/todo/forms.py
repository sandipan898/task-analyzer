from django import forms
from .models import List


class ListForm(forms.ModelForm):
    name = forms.CharField(
        label="Task Name", 
        required=False, 
        max_length=500, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    weight = forms.IntegerField(
        label="Priority", 
        required=False, 
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = List
        fields = ["name", "weight", ]
        