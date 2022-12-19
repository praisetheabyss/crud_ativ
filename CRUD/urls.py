"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from unicodedata import name
from django.contrib import admin
from django.urls import path
from AppCRUD.views import listarAutores, criarAutores, editarAutores, deletarAutores, home, listarArtigos, criarArtigos, editarArtigos, excluirArtigos, listarEdicoes, criarEdicoes, editarEdicoes, excluirEdicoes, listarLinguagens, criarLinguagens, editarLinguagens, excluirLinguagens

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_index'),
    path('listar_autores/', listarAutores, name='url_listar_autores'),
    path('form_autores/', criarAutores, name='url_criar_autor'),
    path('editar_autor/<int:pk>/', editarAutores, name='url_editar_autor'),
    path('excluir_autor/<int:pk>/', deletarAutores, name='url_deletar_autor'),

    path('listar_artigos/', listarArtigos, name='url_listar_artigos'),
    path('form_artigos/', criarArtigos, name='url_criar_artigo'),
    path('editar_artigo/<int:pk>/', editarArtigos, name='url_editar_artigo'),
    path('excluir_artigo/<int:pk>/', excluirArtigos, name='url_excluir_artigo'),

    path('listar_edicoes/', listarEdicoes, name='url_listar_edicoes'),
    path('form_edicoes/', criarEdicoes, name='url_criar_edicao'),
    path('editar_edicao/<int:pk>/', editarEdicoes, name='url_editar_edicao'),
    path('excluir_edicao/<int:pk>/', excluirEdicoes, name='url_excluir_edicao'),

    path('listar_linguagens/', listarLinguagens, name='url_listar_linguagens'),
    path('form_linguagens/', criarLinguagens, name='url_criar_linguagem'),
    path('editar_linguagem/<int:pk>/', editarLinguagens, name='url_editar_linguagem'),
    path('excluir_linguagem/<int:pk>/', excluirLinguagens, name='url_excluir_linguagem'),
]
