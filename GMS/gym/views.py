from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


# Create your views here.
def Home(request):
    return render(request, 'login.html')


def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')