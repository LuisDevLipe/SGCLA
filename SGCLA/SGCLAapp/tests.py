from django.test import TestCase
from .views import adicionarUmLivro, resultadoDaBusca
from .models import Livro 
from django.test.client import RequestFactory
from django.db.models import Q

# Create your tests here.

class ResultadoDaBusa(TestCase):
    def setUp(self):
        self.factory=RequestFactory()
    
    def test_busca(self):
        self.assertContains("A metamorfose")