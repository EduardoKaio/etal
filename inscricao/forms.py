from inscricao.models import *
from django import forms


class DatePickerInput(forms.DateInput):
        input_type = 'date'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class ParticipanteForm(forms.ModelForm):
    
     class Meta:
        model=Participante
        fields= '__all__'   
        
        widgets = {
             'nome': forms.TextInput(attrs={'class': 'form-control'}),
             'cpf': forms.TextInput(attrs={'class': 'form-control'}),
             'email': forms.TextInput(attrs={'class': 'form-control'}),
             'endereco': forms.TextInput(attrs={'class': 'form-control'}),
             'curso': forms.Select(attrs={'type': 'select', 'class': 'form-control'}),
             'minicursos': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox', 'class': ''}),
             'sexo': forms.RadioSelect(attrs={'type': 'radio', 'class': ''}),
             'data_nascimento': forms.TimeInput(attrs={'type': 'date', 'class': 'form-control'}),
         }

