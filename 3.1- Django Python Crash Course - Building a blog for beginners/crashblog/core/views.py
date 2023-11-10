from django.shortcuts import render

from blog.models import Post


def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'core/frontpage.html', {'posts': posts})

def about(request):
    return render(request, 'core/about.html')

def chamados(request):
    return render(request, 'core/chamados.html')

def conta(request):
    return render(request, 'core/conta.html')

def estoque(request):
    return render(request, 'core/estoque.html')

