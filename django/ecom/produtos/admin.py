from django.contrib import admin
from produtos.models import Produto

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    prepopulated_fields= {
            'slug' : ('produto_nome',),
    }
    list_display= ('produto_nome','preco', 'esta_disponivel')

admin.site.register(Produto, ProdutoAdmin)