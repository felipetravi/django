from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Oi, negão.')


def contato(request):
    return HttpResponse('E-mail: fltravi@gmail.com')


def sobre(request):
    return HttpResponse('Exercícios Django :)')



