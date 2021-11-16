from django.http import HttpResponse
from django.template.loader import get_template

def proveedores(request):

    page = get_template('subpaginas/proveedores.html')
    page_render = page.render()
    return HttpResponse(page_render)

def nuevoPro(request):

    page = get_template('subpaginas/nuevoPro.html')
    page_render = page.render()
    return HttpResponse(page_render)