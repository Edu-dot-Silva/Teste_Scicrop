from django.shortcuts import get_object_or_404, render
from blog.models import Posts

# Create your views here.
def lista_posts(request):
    template_name = 'lista_posts.html'
    posts = Posts.objects.all()
    context = {
        'posts':posts
    }
    return render (request,template_name,context)


from django.urls import reverse
from django.http import HttpResponseRedirect
from blog.forms import FormularioPost
from django.contrib import messages

def criar_postagem(request):
    if request.method == 'POST':
        formulario = FormularioPost(request.POST, request.FILES)
        if formulario.is_valid():
            formulario = formulario.save(commit=False)
            formulario.save()

            messages.success(request, f"Postagem '{formulario.titulo}' adicionada!")
            return HttpResponseRedirect(reverse('lista_posts'))
        
    formulario = FormularioPost()
    return render(request, 'formulario_postagem.html',{"formulario": formulario})


def abrir_post(request, id):
    template_name = 'post_aberto.html'
    postagem = Posts.objects.get(id = id)
    print(postagem)
    context = {
        'postagem': postagem
        }
    return render (request, template_name, context)


def edita_post(request,id):
    postagem = get_object_or_404(Posts, id=id)
    formulario = FormularioPost(request.POST or None,request.FILES or None, instance=postagem)
    if formulario.is_valid():
        formulario.save()

        messages.success(request, f"Postagem '{postagem.titulo}' atualizada!" )
        return HttpResponseRedirect(reverse('abrir_post',args=[postagem.id]))
    
    return render(request,'formulario_postagem.html',{"formulario": formulario})


def deleta_postagem(request,id):
    postagem = Posts.objects.get(id=id)
    if request.method == 'POST':
        postagem.delete()
        messages.success(request, f"Postagem '{postagem.titulo}' deletada!")
        return HttpResponseRedirect(reverse('lista_posts'))
    return render(request, 'deletar_postagem.html',{"postagem":postagem})