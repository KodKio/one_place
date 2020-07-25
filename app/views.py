from django.shortcuts import render


# Create your views here.
def home_page(request):
    context = dict()
    context['title'] = "Home Page 1"
    return render(request, 'index.html', context)
