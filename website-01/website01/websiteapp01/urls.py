# websiteapp01.py
from django.conf.urls import url
from websiteapp01 import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
	url(r'^about/$', views.AboutPageView.as_view()),
	url(r'^detail/$', views.DetailPageView.as_view()),
]