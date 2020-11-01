from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "pages/aboutme.html"
    #num = 100
#def view_function(request):
    #html = "<h1>Hello World <h1>"
    #return HttpResponse(html)

