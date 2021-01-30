from django.http import HttpResponse
from django.shortcuts import render


def home(reqest):
    name = 'Bob'

    return render(reqest, 'home.html', {'name': name})