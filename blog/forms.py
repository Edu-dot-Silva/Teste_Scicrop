from django import forms
from .models import Posts

class FormularioPost(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['titulo','descricao','imagem']