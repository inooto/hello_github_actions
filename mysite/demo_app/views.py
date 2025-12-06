from django.shortcuts import render
from django.views.generic import TemplateView

class Hello(TemplateView):
    template_name = 'home.html'

