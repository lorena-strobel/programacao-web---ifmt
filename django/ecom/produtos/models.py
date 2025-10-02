from django.db import models
from django.urls import reverse

from categoria.models import Categoria

# Create your models here.
class Produto(models.Model):
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    produto_nome = models.CharField(max_length=150, unique=True)
    descricao= models.TextField(max_length=400, blank=True)
    preco = models.DecimalField(decimal_places=2, max_digits=11)
    imagem = models.ImageField(upload_to='fotos/produtos')
    estoque = models.IntegerField()
    slug = models.SlugField(max_length=200, unique=True)
    esta_disponivel= models.BooleanField(default=True)
    data_alteracao = models.DateTimeField(auto_now_add=True)
    data_criacao = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('detalhes_do_produto',args=[self.categoria.slug, self.slug])