from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.utils import timezone
from .models import Livro, LivrosAlugados, Usuario
from django.urls import reverse
import datetime
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
    alugados = LivrosAlugados.objects.filter(livro_id = livro_id)
    livrosDisponiveis = livro.unidades - alugados.count()
    return render(request, "SGCLAapp/detalhes.html",{
        "livro": livro,
        "alugados": alugados,
        "disponiveis":livrosDisponiveis,
    })

def resultadoDaBusca(request,busca):

    busca = request.GET["titulo"]
    livros = list(Livro.objects.filter(titulo__icontains = busca))
    livros += Livro.objects.filter(autor__icontains = busca)

    return render(
        request,
        "SGCLAapp/index.html",
        {
            "livros":livros,
            "busca" : True
        }
    )

def adicionarUmLivroRota(request):
    template = loader.get_template("SGCLAapp/adicionarUmLivro.html")
    contexto = {"fakeIt_tillYouMakeIt" : True}
    return  HttpResponse(template.render(contexto, request))

def adicionarUmLivro(request):
    if int(request.POST["unidades"]) <= 0:
        raise ValueError("As unidades precisam ser um número válido maior que 0.")
    
    livro, inserido = Livro.objects.get_or_create(
        titulo=request.POST["titulo"],
        genero=request.POST["genero"],
        autor=request.POST["autor"],
        editora=request.POST["editora"],
        anoPublicacao=request.POST["anoPublicacao"],      
        unidades=int(request.POST["unidades"])
    )

    if inserido:
        return HttpResponseRedirect(
            reverse(
                "SGCLA:detalhes",
                kwargs={"livro_id":livro.id}
            )
        )
    
    else:
        return render(
                request,
                "SGCLAapp/detalhe.html",
                {
                    "livro":livro,
                    "mensagemDeErro":"Este livro já consta na base de dados"
                },
            )