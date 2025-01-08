from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('criar_postagem/',views.criar_postagem, name='criar_postagem'),
    path('postagem/<int:id>/',views.abrir_post, name='abrir_post'),
]