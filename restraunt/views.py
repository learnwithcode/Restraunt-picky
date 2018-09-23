from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import RestrauntLocation
# Create your views here.


def restraunt_list(request):
    queryset = RestrauntLocation.objects.all()  
    context = {
        "title": "Restraunts",
        "objects": queryset
    }
    return render(request, "restraunt.html", context) 

class AboutView(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, *args, **Kwargs):
        context = super(AboutView, self).get_context_data(*args, **Kwargs)
        context = {
            "title": "About Page",
        }
        return context   

class ContactView(TemplateView):
    template_name = 'contact.html'
    def get_context_data(self, *args, **Kwargs):
        context = super(ContactView, self).get_context_data(*args, **Kwargs)
        context = {
            "title": "Contact Page",
        }
        return context      
