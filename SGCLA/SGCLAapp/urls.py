from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detalhes/<int:livro_id>",views.detalhes, name="detalhes"),
    path("<str:busca>/", views.buscaDeLivros, name="busca")
]