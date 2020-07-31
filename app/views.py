from django.shortcuts import render
import app.parsers as parse


# Create your views here.
def home_page(request):
    context = dict()
    dtfparse = parse.DTFParser()
    context['title'] = "Home Page 1"
    return render(request, 'index.html', context)

