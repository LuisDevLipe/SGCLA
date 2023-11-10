from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from django.utils import timezone
from .models import Livro
from django.template import loader


# Create your views here.

def index(request):
    livros = Livro.objects.all().order_by("titulo")
    template = loader.get_template("SGCLAapp/index.html")
    context = {
        "livros":livros
    }
    return HttpResponse(template.render(context, request))

def detalhes(request,livro_id):
    livro = get_object_or_404(Livro, pk = livro_id)
    return render(request, "SGCLAapp/detalhe.html",{
        "livro": livro
    })

def buscaDeLivros(request,busca):
    livros = Livro.objects.filter(titulo__contains = busca)
    saida = ", ".join([l.titulo + "-" + l.autor for l in livros])
    return HttpResponse(
        "Lista de livros pesquisados" + " Com o termo " + saida
    )