# Create your views here.
from django.shortcuts import render,redirect
# imported our models
from django.core.paginator import Paginator
from . models import Song



def index(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)
def about(request):
    return render(request, 'earth.html')
def eng(request):
    return render(request, 'moon.html')
def lol(request):
    return render(request, 'solar.html')
def star(request):
    return render(request, 'star.html')