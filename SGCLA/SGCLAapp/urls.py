from django.urls import path
from . import views

app_name = "SGCLA"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:livro_id>/detalhes/" ,views.detalhes, name="detalhes"),
    path("resultadoDaBusca/<str:busca>", views.resultadoDaBusca, name="buscar"),
    path("adicionarUmLivroRota/", views.adicionarUmLivroRota, name="adicionarUmLivroRota"),
    path("adicionarUmLivro/", views.adicionarUmLivro, name="adicionarUmLivro")
]