from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from .models import Livro, LivrosAlugados
from django.db.models import Q
from django.urls import reverse
from django.template import loader
from django.core.exceptions import ValidationError


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
        livros = Livro.objects.filter( Q(titulo__icontains = busca) | Q(autor__icontains = busca))
        if livros:
            statusCode = 201
        else:
            statusCode = 404
        return render(
            request,
            "SGCLAapp/index.html",
            {
                "livros":livros,
                "busca" : True
            },
            status = int(statusCode)
        )
def adicionarUmLivroRota(request):
    template = loader.get_template("SGCLAapp/adicionarUmLivro.html")
    contexto = {"fakeIt_tillYouMakeIt" : True}
    return  HttpResponse(template.render(contexto, request))

def adicionarUmLivro(request):

    if request.POST["unidades"]:
        entradasInvalidas = ["True", "None", "False"]
        if request.POST["unidades"] in entradasInvalidas:
            raise ValidationError("Seu filho da ****",500)
        if int(request.POST["unidades"]) <= 0:
            raise ValidationError("As unidades precisam ser um número válido maior que 0.", 500)
        
    templateForm = loader.get_template("SGCLAapp/adicionarUmLivro.html")
    contexto = {
        "erro":
            "O campo unidades precisa ser um número inteiro válido maior que zero"
    }

    if int(request.POST['unidades']) <= 0:
        return HttpResponse(templateForm.render(
            contexto, request
        ))
    else:
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
                    kwargs={
                        "livro_id":livro.id,
                        }
                )
            )
        
        else:
            return render(
                    request,
                    "SGCLAapp/detalhes.html",
                    {
                        "livro":livro,
                        "mensagemDeErro":"Este livro já consta na base de dados"
                    },
                )