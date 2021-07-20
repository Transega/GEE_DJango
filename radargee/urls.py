from django.urls import path
# from django.views.generic import TemplateView
from django.shortcuts import render,HttpResponse

from radargee.views import home

urlpatterns= [
    path('', home.as_view(template_name="index.html")),
]