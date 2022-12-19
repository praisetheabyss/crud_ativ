from django.shortcuts import render, redirect
from .models import *
from .form import *
# Create your views here.
def home(request):
    return render(request, 'AppCRUD/index.html')

# Autores
def listarAutores(request):
    data = {}
    data['autores'] = Autor.objects.all()
    return render(request, 'AppCRUD/Autores/listar.html', data)

def criarAutores(request):
    data = {}
    form = AutorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listar_autores')

    data['form'] = form
    return render(request, 'AppCRUD/Autores/criar_ed.html', data)

def editarAutores(request, pk):
    autor = Autor.objects.get(pk=pk)
    form = AutorForm(request.POST or None, instance=autor)
    
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_listar_autores')

    data['form'] = form
    return render(request, 'AppCRUD/Autores/criar_ed.html', data)

def deletarAutores(request, pk):
    autor = Autor.objects.get(pk=pk)
    autor.delete()
    return redirect('url_listar_autores')

# Artigos
def listarArtigos(request):
    data = {}
    data['artigos'] = Artigo.objects.all()
    return render(request, 'AppCRUD/Artigos/listar.html', data)

def criarArtigos(request):
    data = {}
    form = ArtigoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listar_artigos')

    data['form'] = form
    return render(request, 'AppCRUD/Artigos/criar_ed.html', data)

def editarArtigos(request, pk):
    artigo = Artigo.objects.get(pk=pk)
    form = ArtigoForm(request.POST or None, instance=artigo)
    
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_listar_artigos')

    data['form'] = form
    return render(request, 'AppCRUD/Artigos/criar_ed.html', data)

def excluirArtigos(request, pk):
    artigo = Artigo.objects.get(pk=pk)
    artigo.delete()
    return redirect('url_listar_artigos')

# Edições
def listarEdicoes(request):
    data = {}
    data['edicoes'] = Edicao.objects.all()
    return render(request, 'AppCRUD/Edicoes/listar.html', data)

def criarEdicoes(request):
    data = {}
    form = EdicaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listar_edicoes')

    data['form'] = form
    return render(request, 'AppCRUD/Edicoes/criar_ed.html', data)

def editarEdicoes(request, pk):
    edicao = Edicao.objects.get(pk=pk)
    form = EdicaoForm(request.POST or None, instance=edicao)
    
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_listar_edicoes')

    data['form'] = form
    return render(request, 'AppCRUD/Edicoes/criar_ed.html', data)

def excluirEdicoes(request, pk):
    edicao = Edicao.objects.get(pk=pk)
    edicao.delete()
    return redirect('url_listar_edicoes')

# Linguagens
def listarLinguagens(request):
    data = {}
    data['linguagens'] = Linguagem.objects.all()
    return render(request, 'AppCRUD/Linguagens/listar.html', data)

def criarLinguagens(request):
    data = {}
    form = LinguagemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listar_linguagens')

    data['form'] = form
    return render(request, 'AppCRUD/Linguagens/criar_ed.html', data)

def editarLinguagens(request, pk):
    linguagem = Linguagem.objects.get(pk=pk)
    form = LinguagemForm(request.POST or None, instance=linguagem)
    
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_listar_linguagens')

    data['form'] = form
    return render(request, 'AppCRUD/Linguagens/criar_ed.html', data)

def excluirLinguagens(request, pk):
    linguagem = Linguagem.objects.get(pk=pk)
    linguagem.delete()
    return redirect('url_listar_linguagens')
