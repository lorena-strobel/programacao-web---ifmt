from django.contrib import admin

from categoria.models import Categoria

# Register your models here.
# classe para permitir uma apresentação de atributos e atribuição automática de dados para o slug 
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ('categoria_nome',)
    }

    list_display=('categoria_nome','slug')
admin.site.register(Categoria,CategoriaAdmin)