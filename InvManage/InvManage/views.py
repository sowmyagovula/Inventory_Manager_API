from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return HttpResponse("<h1>Welcome to Home page</h1>")
