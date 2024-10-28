from django.shortcuts import render, redirect
from distribuidorApp.forms import formDistribuidor
from distribuidorApp.models import Distribuidor

# Create your views here.
def index(request):
    return render(request, 'distribuidorApp/index.html')

def listadoDistribuidor(request):
    distribuidores = Distribuidor.objects.all()
    data = {'distribuidores': distribuidores}
    return render(request, 'distribuidorApp/distribuidores.html', data)

def agregarDistribuidor(request):
    form = formDistribuidor()
    if request.method == 'POST':
        form = formDistribuidor(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'distribuidorApp/agregarDistribuidor.html', data)

def eliminarDistribuidor(request, id):
    distribuidor = Distribuidor.objects.get(id=id)
    distribuidor.delete()
    return redirect('/distribuidores')

def actualizarDistribuidores(request, id):
    distribuidor = Distribuidor.objects.get(id=id)
    form = formDistribuidor(instance=distribuidor)
    if request.method == 'POST':
        form = formDistribuidor(request.POST, instance=distribuidor)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'distribuidorApp/agregarDistribuidor.html', data)