from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "title": "Home Page",
    }
    return render(request, "base.html", context)
