from django.shortcuts import render
from inscricao.forms import *
from django.contrib import messages
from django.contrib.messages import constants

def index(request):
    if request.method == 'POST':
        form = ParticipanteForm(request.POST) 
        if form.is_valid():
            form.save()
            form = ParticipanteForm()
            print('Salvou')
            # messages.success(request, 'Inscrição realizada com sucesso')
            messages.add_message(request, constants.SUCCESS, 'Inscrição realizada com sucesso!')
        else:
            messages.error(request, 'Ocorreu um erro na sua inscrição.') 
    else:
        form = ParticipanteForm()
        
    return render(request,'index.html', { 'form' : form})

