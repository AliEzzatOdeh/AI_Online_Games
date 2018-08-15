from django.http import HttpResponse
from django.template.loader import get_template
# Create your views here.
def index(request):
    my_template = get_template('index.html')
    html = my_template.render()
    return HttpResponse(html)