from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "title": "Home Page",
    }
    return render(request, "home.html", context)


def contact(request):
    context = {
        "title": "Contact Page",
    }
    return render(request, "contact.html", context)


def about(request):
    context = {
        "title": "About Page",
    }
    return render(request, "about.html", context)