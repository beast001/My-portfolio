from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home_page/index.html', context={"title": "hellow world"})