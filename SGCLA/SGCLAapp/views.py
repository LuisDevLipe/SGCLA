from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


# Create your views here.

def index(request):
    time = timezone.now()
    return HttpResponse(
        "Sistema de gerenciamento e controle de livros alugados - SGCLA - em django Framework" + str(time)
        )