from django.http import HttpResponse
from django.template.loader import get_template

def home(request):

    page = get_template('paginas/home.html')
    page_render = page.render()
    return HttpResponse(page_render)

def añadir(request):

    page = get_template('subpaginas/añadir.html')
    page_render = page.render()
    return HttpResponse(page_render)