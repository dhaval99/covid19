from django.shortcuts import render
from django.http import HttpResponse
from data import kvpairs, orig_pairs
# Create your views here.


def home(request):
    return render(request, 'index.html', {'dropdown': orig_pairs})


def info(request):
    country = request.POST['cName'].lower().strip()
    send = " "
    if country == "usa" or country == "united states of america":
        country = "us"
    elif country == "uk":
        country = "united kingdom"
    elif country == "uae":
        country = "united arab emirates"
    elif country == "south korea":
        country = "korea, south"
    for i in kvpairs:
        if i == country:
            send = kvpairs[i]
    return render(request, "jinja.html", {'number': send})
