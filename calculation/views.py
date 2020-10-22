from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class CalculationViewTemplate(TemplateView):
    template_name = "pages/calc.html"