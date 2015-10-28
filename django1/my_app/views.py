from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    context = dict()
    return render(request, "home.html", context)

def home(request):
    context = dict()
    return render(request,"home.html",context)

def guest(request):
    context = dict()
    return render(request,"guest.html",context)

def loggedIn(request):
    context = dict()
    context['Welcome'] = "Really? "
    return render(request,"loggedIn.html",context)