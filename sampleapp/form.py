from django import forms
from .models import log

class AddForm(forms.ModelForm):
    class Meta:
        model = log
        fields = ('username','age','email','password','conform_password')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            'conform_password': forms.TextInput(attrs={'class':'form-control'}),
        }