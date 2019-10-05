from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


# Create your views here.
def home(request):
    return render(request, 'index.html')


def new_search(request):
    search = request.POST['search']
    stuff_for_frontend = {'search': search}
    return render(request, 'myapp/new_search.html', stuff_for_frontend)

