from django import forms
from .models import Grant




class DateInput(forms.DateInput):
    input_type = 'date'

class GrantForm(forms.ModelForm):

    class Meta:
        model = Grant
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Grant nomi', 'required': True}),
            'description': forms.TextInput(attrs={'placeholder': 'Grant haqida tavsif', 'required': True}),
            'first_science': forms.TextInput(attrs={'placeholder': 'Birinchi fan', 'required': True}),
            'second_science': forms.TextInput(attrs={'placeholder': 'Ikkinchi fan', 'required': True}),
            'third_science': forms.TextInput(attrs={'placeholder': 'Uchinchi fan', 'required': True}),
            'statute': forms.FileInput(attrs={'required': True}),
            

            'start_date': DateInput(),
            'end_date': DateInput(),
            'create_at': DateInput(),
        }


