from django.test import TestCase
from .views import adicionarUmLivro
from django.test.client import RequestFactory
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your tests here.

class AdicionarLivroTest(TestCase):
    
    def test_unidades_menor_ou_igual_zero(self):
        valores = [0, -2, -42, "-42", "-2", "0", "True", "None", "False"]
        for valor in valores:
            with self.assertRaises(ValidationError):
                rf = RequestFactory().post(
                    "SGCLA:adicionarUmLivro",
                    {
                        "titulo":"testeUnidades",
                        "autor":"testeUnidades",
                        "genero":"testeUnia",
                        "editora":"testeUnidades",
                        "anoPublicacao":timezone.now(),
                        "unidades": valor
                    },)
                adicionarUmLivro(request=rf)