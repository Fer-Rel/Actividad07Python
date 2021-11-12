from math import *
from django.http import HttpResponse
from django.template.loader import get_template

def Home(request):

    page = get_template('paginas/home.html')
    page_render = page.render()
    return HttpResponse(page_render)