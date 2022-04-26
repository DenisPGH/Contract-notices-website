from django.shortcuts import render
from django.views import generic as views

# Create your views here.



class ViewPage(views.TemplateView):
    template_name = 'index_a.html'


