from django.shortcuts import render
import app.parsers as parse


# Create your views here.
def home_page(request):
    context = dict()
    dtf = parse.DTFParser()
    dtf_news = dtf.get_all()
    context['dft_news'] = []
    j = 0
    row = []
    for i in range(len(dtf_news)):
        if j < 3:
            row.append(dtf_news[i])
            j += 1
        else:
            context['dft_news'].append(row)
            j = 0
            row = []
    if len(row):
        context['dft_news'].append(row)
    context['title'] = "DTF"
    return render(request, 'index.html', context)

