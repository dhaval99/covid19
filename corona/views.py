from django.shortcuts import render
from django.http import HttpResponse
from data import kvpairs
# Create your views here.


def home(request):
    return render(request, 'index.html')

def info(request):
    country = request.POST['cName']
    send = " "
    for i in kvpairs:
        if i == country:
            send = kvpairs[i]
    return render(request, "jinja.html", {'number': send})