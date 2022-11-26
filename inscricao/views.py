from django.shortcuts import render
from inscricao.forms import *

def index(request):
    if request.method == 'POST':
        form = ParticipanteForm(request.POST) 
        if form.is_valid():
            form.save()
            form = ParticipanteForm()
            print('Salvou')
    else:
        form = ParticipanteForm()

    return render(request,'index.html', { 'form' : form})

