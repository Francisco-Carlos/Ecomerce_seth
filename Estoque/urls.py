from django.contrib import admin
from django.urls import path
from Estoque.views import *
urlpatterns = [
    path('', Index,name='Index'),
    path('Compra/int<id>', Compra, name='Compra'),
    path('Descricao/int<id>',Descricao,name='Descricao'),
    path('Produto/str<tipo>',Protudo,name='Produto'),
    path('Cadastrar', Cadastro,name='Cadastrar'),
    path('Login',Login, name='Login'),
    path('Dashbord',Dashbord,name='Dashbord'),
    path('Sair',Sair,name='Sair'),
    path('Login_adm',Login_adm,name='Login_adm'),
    path('Dashbord_adm',Loja,name='Dashbord_adm'),
    path('Forncedor',Fornecedor,name='Fornecedor'),
]