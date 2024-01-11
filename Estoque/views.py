from django.shortcuts import render, redirect, get_object_or_404
from .models import Estoque, Empresa_lucro, Clientes
from datetime import datetime
from .utils import get_estoq, get_lucro

from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def Index(request):
    produto = Estoque.objects.all()
    context = {'produto': produto}
    return render(request, 'index.html', context)


def Descricao(request, id):
    prod = Estoque.objects.get(id=id)
    list_prod = Estoque.objects.all().exclude(id=id)
    context = {'produto': prod, 'list_prod': list_prod}
    return render(request, 'descricao.html', context)


def Protudo(request, tipo):
    tecl = Estoque.objects.filter(Nome_produto__icontains=tipo)
    context = {'teclado': tecl}
    return render(request, 'Teclados.html', context)


def Compra(request, id):
    if request.user.is_authenticated:
        produto = Estoque.objects.get(id=id)
        Empresa = Empresa_lucro.objects.all()
        ids = request.user.id
        User_c = get_object_or_404(User,pk = ids)
        Clinte = Clientes.objects.all()
        if request.method == 'POST':
            quant = request.POST['Qt']
            produto.Quantidade = produto.Quantidade - int(quant)
            produto.save()

            data_t = datetime.today().strftime('%d/%m/%Y')
            data_cop = datetime.today()
            print(data_t)
            val = produto.preco * int(quant)
            for x in Empresa:
                if x.Nome_do_produto == produto.Nome_produto and str(x.Data) == data_t:
                    x.Valor = x.Valor + val
                    x.save()
                    return redirect('/')
            Empr = Empresa_lucro.objects.create(
                Nome_do_produto=produto.Nome_produto, Valor=val, Data=data_cop)
            Empr.save()
            Clinte = Clientes.objects.create(Nome=User_c,Produto=produto.Nome_produto,Endereco='avenida')
            Clinte.save()


            return redirect('/')
# Aqui e para fazer o login tanto de usuarios quanto normal.


def Cadastro(request):
    if request.method == 'POST':
        nome = request.POST['Nome']
        email = request.POST['Email']
        senha = request.POST['Senha']
        senha_cof = request.POST['Senha_1']

        if User.objects.filter(email=email).exists():
            return redirect('Index')
        if senha != senha_cof:
            return redirect('Cadastrar')

        user = User.objects.create_user(
            username=nome, email=email, password=senha)
        user.save()
        return redirect('Dashbord')
    else:
        return render(request, 'Cadastrar.html')


def Login(request):
    if request.method == 'POST':
        email = request.POST['Email']
        senha = request.POST['Senha']
        if email == '' or senha == ' ':
            redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list(
                'username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('Dashbord')
    return render(request, 'Login.html')

def Sair(request):
    auth.logout(request)
    return redirect('Index')

def Dashbord(request):
    if request.user.is_authenticated:
        id = request.user.id
        Clin = Clientes.objects.all().filter(Nome=id)
        Prod = Estoque.objects.all()
        context = {'Clin': Clin,'Prod':Prod}
        return render(request, 'Dashbord.html', context)
# Aqui e para fazer o login tanto adm .


def Login_adm(request):
    if request.method == 'POST':
        email = request.POST['Email']
        senha = request.POST['Senha']
        if email == '' or senha == ' ':
            redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list(
                'username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('Dashbord_adm')
    return render(request, 'Login_adm.html')


# Aqui e a parte do ganho da loja e o controle do estoque.
def Loja(request):
    if request.user.is_authenticated:
        Estoq = Estoque.objects.all()
        Lucro = Empresa_lucro.objects.all()

        x = [x.Data for x in Lucro]
        y = [y.Valor for y in Lucro]
        Grafico_luc = get_lucro(x, y)

        u = [u.Nome_produto for u in Estoq]
        w = [w.Quantidade for w in Estoq]
        Grafico_est = get_estoq(u, w)

        context = {'estoque': Estoq, 'Lucro': Lucro,
                   'Grafico_luc': Grafico_luc, 'Grafico_esq': Grafico_est}
        return render(request, 'Dashbord_adm.html', context)


def Fornecedor(request):
    if request.method == 'POST':
        NomProduto = request.POST['prod_list']
        Quant = request.POST['Quant']
        aux = Estoque.objects.get(id=NomProduto)

        aux.Quantidade = aux.Quantidade + int(Quant)
        aux.save()
        return redirect('Dashbord_adm')
