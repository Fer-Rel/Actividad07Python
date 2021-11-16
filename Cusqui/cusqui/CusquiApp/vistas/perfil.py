from django.http import HttpResponse
from django.template.loader import get_template

def perfil(request):

    page = get_template('subpaginas/perfil.html')
    page_render = page.render()
    return HttpResponse(page_render)