from django.shortcuts import render
from .parsers import modules as parse


# Create your views here.
def home_page(request):
    context = dict()
    dtf = parse.DTFParser()
    dtf_news = dtf.get_all()
    context['dft_news'] = []
    for i in range(len(dtf_news) // 3):
        context['dft_news'].append([])
    if len(dtf_news) % 3 != 0:
        context['dft_news'].append([])
    for i in range(len(dtf_news)):
        context['dft_news'][i // 3].append(dtf_news[i])
    context['title'] = "DTF"
    return render(request, 'index.html', context)

