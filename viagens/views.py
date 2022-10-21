from django.shortcuts import render
from viagens.forms import ViagemForms

def index(request):
    form = ViagemForms()
    contexto = {'form': form}
    return render( request, 'index.html', contexto)

def revConsulta (request):
    if request.method == 'POST':
        form = ViagemForms (request.POST)
        if form.is_valid():
            contexto = { 'form': form}
            return render (request, 'consulta.html', contexto)
        else:
            print('form inválido')
            contexto = {'form': form}
            return render(request, 'index.html', contexto)



