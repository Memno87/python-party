#websiteapp01/views.py

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
#class HomePageView(TemplateView):
		#def get(self, request, **kwargs):
			#return render(request, 'index.html', context=None)

# Homepage alternative
class HomePageView(TemplateView):
	template_name = "index.html"

# About screen view
class AboutPageView(TemplateView):
	template_name = "about.html"

# Further details page
class DetailPageView(TemplateView):
	template_name = "detail.html"