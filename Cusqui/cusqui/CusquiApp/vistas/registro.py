from django.http import HttpResponse
from django.template.loader import get_template

def registro(request):

    page = get_template('paginas/registro.html')
    page_render = page.render()
    return HttpResponse(page_render)