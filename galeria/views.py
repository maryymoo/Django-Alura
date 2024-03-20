from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from galeria.models import Fotografia

# Create your views here.
def index(request):
 
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) #Pegando todas as fotos que estão publicadas

    return render(request, 'galeria/index.html', {"cards" : fotografias})

def imagem(request, foto_id): #Pegando o id da foto
    #Pegando o objeto que corresponde ao id
    fotografia = get_object_or_404(Fotografia, pk=foto_id) 
    #Passando o objeto para o template
    return render(request, 'galeria/imagem.html', {"fotografia" : fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) #Pegando todas as fotos que estão publicadas
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'galeria/buscar.html', {"cards" : fotografias})
