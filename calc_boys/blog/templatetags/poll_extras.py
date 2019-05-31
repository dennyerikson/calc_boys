from django import template
from accounts.models import Pessoa

register = template.Library()

@register.filter
def get_foto(id):
    """Get id e retorna o url da imagem"""    
    pessoa = Pessoa.objects.get(user=id)
    return pessoa.foto.url