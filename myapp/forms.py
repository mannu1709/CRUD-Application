from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = ['name','roll','city']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name',
                'autofocus': True, 
            }),
            'roll': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter roll number',
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter city name',
            }),
        }