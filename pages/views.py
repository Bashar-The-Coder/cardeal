from django.shortcuts import render, HttpResponse
from pages.models import Team
# Create your views here.
def home(request):
    teams = Team.objects.all()
    data = {
        "teams" : teams
    }
    return render (request, 'pages/home.html',data)
    

def about(request):
    teams = Team.objects.all()
    data = {
        "teams" : teams
    }
    return render (request, 'pages/about.html' , data)

def detail(request, id):
    person = Team.objects.get(pk=id)
    return render (request, 'pages/detail.html' , {"data" : person})

def services(request):
    return render (request, 'pages/services.html')

def contact(request):
    return render (request, 'pages/contact.html')

