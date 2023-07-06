from django import forms
from .models import Faculty, SubFaculty, PRINTED, Message


class DateInput(forms.DateInput):
    input_type = 'date'


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fakultet nomi', 'required': True}),
            'create_at': DateInput(),
        }


class SubFacultyForm(forms.ModelForm):
    class Meta:
        model = SubFaculty
        fields = ['name', 'faculty']



class MessageForm(forms.ModelForm):

    class Meta: 
        model = Message
        fields = ('student', 'article', 'win', 'letter')
        widgets = {
            'article': forms.Select(attrs={'id': 'article-select', 'style': 'display: none'}),
            'win': forms.Select(attrs={'id': 'win-select', 'style': 'display: none'}),
        }