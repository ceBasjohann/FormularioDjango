from django.shortcuts import render, redirect
from form.forms import CarrosForm
from form.models import Carros #Importação do modelo de formulario


def home (request):#Essa função pega os dados do banco e joga para o index.html
    data = {}
    data['db'] = Carros.objects.all()
    return render(request, 'index.html', data)

def form(request):#Essa função renderiza o formulario
    data = {}
    data ['form'] = CarrosForm()
    return render(request, 'form.html', data)

def create(request):#Essa função pega os dados digitados no  formulario do form.html e salva no banco de dados
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')