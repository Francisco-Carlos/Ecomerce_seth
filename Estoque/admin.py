from django.contrib import admin
from Estoque.models import Estoque,Empresa_lucro,Clientes
# Register your models here.
class ListEstoque(admin.ModelAdmin):
    list_display = ('Nome_produto','Descricao', 'preco','Quantidade')

class ListEmpresa(admin.ModelAdmin):
    list_display = ('Nome_do_produto','Valor','Data')

class ListCliente(admin.ModelAdmin):
    list_display = ('Nome','Produto','Endereco')

admin.site.register(Estoque,ListEstoque)
admin.site.register(Empresa_lucro,ListEmpresa)
admin.site.register(Clientes,ListCliente)