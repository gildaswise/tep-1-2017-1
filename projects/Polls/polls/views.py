from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')

def question(request, pk):
    qst = Question.objects.get(pk=pk)
    return render(request, 'question.html', {"question": qst})
