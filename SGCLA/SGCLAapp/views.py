from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Sistema de gerenciamento e controle de livros alugados - SGCLA", "em django Framework")
