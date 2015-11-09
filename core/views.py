from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# inherits from TemplateView
class SplashView(TemplateView):
	template_name = "index.html"
