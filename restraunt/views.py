from django.shortcuts import render
from django.views import View

# Create your views here.

def home(request):
    context = {
        "title": "Home Page",
    }
    return render(request, "home.html", context)

def about(request):
    context = {
        "title": "About Page",
    }
    return render(request, "about.html", context)

class ContactView(View):
    def get(self, request, *args, **Kwargs): # *args, **Kwargs required when working with id
        context = {
            "title": "Contact Page",
        }
        return render(request, "contact.html", context)        
