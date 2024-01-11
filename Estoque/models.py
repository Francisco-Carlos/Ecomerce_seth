from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Estoque(models.Model):
    Nome_produto = models.CharField(max_length=100)
    Descricao = models.TextField()
    preco = models.DecimalField(max_digits=100, decimal_places=2)
    Quantidade = models.IntegerField()
    img = models.ImageField(upload_to=('Img_prod/%d/%m%Y'))

    def __int__(self):
        self.Nome_produto


class Empresa_lucro(models.Model):
    Nome_do_produto = models.CharField(max_length=100)
    Valor = models.DecimalField(max_digits=1000, decimal_places=2)
    Data = models.DateField()


class Clientes(models.Model):
    Nome = models.ForeignKey(User, on_delete=models.CASCADE)
    Produto = models.CharField(max_length=100, blank=True)
    Endereco = models.CharField(max_length=100, blank=True)

    def __int__(self):
        self.Nome
