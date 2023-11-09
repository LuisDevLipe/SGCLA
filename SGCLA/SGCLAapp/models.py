from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField("Título do Livro", max_length=200)
    genero = models.CharField("Gênero textual", max_length=20)
    autor = models.CharField("Autor(res)",max_length=200)
    editora = models.CharField("Editora",max_length=150)
    anoPublicacao = models.DateTimeField("Data de publicação")
    unidades = models.IntegerField(default=1)

    def __str__(self):
        return self.titulo + " - " + str(self.autor)
    

class Usuario(models.Model):
    pNome = models.CharField("Primeiro nome",max_length=200)
    uNome = models.CharField("Sobrenome",max_length=200)
    dataNasc = models.DateField("Data de Nascimento")
    livros = models.ManyToManyField(Livro, through = "LivrosAlugados")

    def __str__(self):
        return self.pNome + ' '+ self.uNome

class LivrosAlugados(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    dataDevolucao = models.DateTimeField()
    dataEmprestado = models.DateTimeField()
    nota = models.CharField("Observação", max_length=200)

    def __str__(self):
        devolve = str(self.dataDevolucao)
        return self.livro.__str__() + "_" + devolve
