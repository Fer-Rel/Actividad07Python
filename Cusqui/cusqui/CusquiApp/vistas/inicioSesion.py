from django.http import HttpResponse
from django.template.loader import get_template

def inicioS(request):

    page = get_template('paginas/inicioSesion.html')
    page_render = page.render()
    return HttpResponse(page_render)