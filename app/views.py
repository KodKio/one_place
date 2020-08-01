from django.shortcuts import render
import app.parsers as parse


# Create your views here.
def home_page(request):
    context = dict()
    dtf = parse.DTFParser()
    context['dft_news'] = dtf.get_all()
    context['title'] = "Home Page 1"
    return render(request, 'index.html', context)

