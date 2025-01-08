from django.db import models

# Create your models here.
class Posts(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens/')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name ='Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']
