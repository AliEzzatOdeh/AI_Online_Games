from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_template = get_template('tic_tac_toe.html')
    html = my_template.render()
    return HttpResponse(html)