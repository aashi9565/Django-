from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req,"home.html")


def about(req):
    return render(req,'about.html')


def contact(req):
    return render(req,'contact.html')