from django.shortcuts import render
from .parsers import modules as parse


# Create your views here.
def home_page(request):
    context = dict()
    dtf = parse.DTFParser()
    dtf_news = dtf.get_all()
    vcru = parse.VCRUParser()
    vcru_news = vcru.get_all()
    context['dtf_news'] = []
    context['vcru_news'] = []
    for i in range(len(dtf_news) // 3):
        context['dtf_news'].append([])
    for i in range(len(vcru_news) // 3):
        context['vcru_news'].append([])
    if len(dtf_news) % 3 != 0:
        context['dtf_news'].append([])
    if len(vcru_news) % 3 != 0:
        context['vcru_news'].append([])
    for i in range(len(dtf_news)):
        context['dtf_news'][i // 3].append(dtf_news[i])
    for i in range(len(vcru_news)):
        context['vcru_news'][i // 3].append(vcru_news[i])
    for i in range(len(context['dtf_news'])):
        item = {
            'index': i,
            'data': context['dtf_news'][i]
        }
        context['dtf_news'][i] = item
    for i in range(len(context['vcru_news'])):
        item = {
            'index': i,
            'data': context['vcru_news'][i]
        }
        context['vcru_news'][i] = item
    print(context)
    return render(request, 'index.html', context)

