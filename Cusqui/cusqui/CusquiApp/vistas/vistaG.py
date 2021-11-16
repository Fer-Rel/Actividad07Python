from django.http import HttpResponse
from django.template.loader import get_template

def vistaG(request):

    page = get_template('subpaginas/vistaG.html')
    page_render = page.render()
    return HttpResponse(page_render)