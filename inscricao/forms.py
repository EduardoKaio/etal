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
             'cpf': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10', 'onkeyup': 'formatarCPF(event)'}),
             'email': forms.TextInput(attrs={'class': 'form-control','pattern' : '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'}),
             'endereco': forms.TextInput(attrs={'class': 'form-control'}),
             'curso': forms.Select(attrs={'type': 'select', 'class': 'form-select'}),
             'minicursos': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox', 'class': 'form-check-input'}),
             'sexo': forms.RadioSelect(attrs={'type': 'radio', 'class': 'form-check-input'}),
             'data_nascimento': forms.TimeInput(attrs={'type': 'date', 'class': 'form-control'}),
         }

