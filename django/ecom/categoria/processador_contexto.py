# método para listar categorias e disponibilizá-las globalmente 
from categoria.models import Categoria

def listarCategorias(request):
    display = Categoria.objects.all()
    return dict(cats = display)