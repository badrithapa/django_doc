from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.style import context
# Create your views here.
def res(request):
    # return HttpResponse("<h1>Hello world. you're at this polls' index.</h1>")
    context = {'name': "badri", 'age':'23'}
    return render(request, 'index.html', context)

def dynamic_view(request, name):
    return HttpResponse(f"<center><h1>Welcome {name}</h1></center>")