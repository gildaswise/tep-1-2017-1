from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *

def index(request):
    return render(request, 'index.html', {"questions": Question.objects.filter(closed=0).order_by("-pub_date")})

def question(request, pk):
    return render(request, 'question.html', {"question": Question.objects.get(pk=pk)})

def vote(request, choice_id):
    choice = Choice.objects.get(pk=choice_id)
    qst = choice.question
    choice.votes = choice.votes + 1
    choice.save()
    return redirect('results', pk=qst.id)

def remove(request, pk):
    qst = Question.objects.get(pk=pk)
    qst.delete()
    return redirect('index')

def results(request, pk):
    qst = Question.objects.get(pk=pk)
    ordered_choices = qst.choices.order_by("-votes")
    return render(request, 'results.html', {"question": Question.objects.get(pk=pk), "choices": ordered_choices})

def manage(request, pk):
    qst = Question.objects.get(pk=pk)
    choices_set = list(map(lambda x: x.id, qst.choices.all()))
    available_choices = Choice.objects.exclude(pk__in=choices_set)
    return render(request, 'manage.html', {"question": qst, "available_choices": available_choices})

def toggle(request, pk):
    qst = Question.objects.get(pk=pk)
    qst.closed = not qst.closed
    qst.save()
    return redirect('manage', pk=pk)

def add_choice(request, pk, choice_id):
    qst = Question.objects.get(pk=pk)
    choice = Choice.objects.get(pk=choice_id)
    qst.choices.add(choice)
    qst.save()
    choice.save()
    return redirect('manage', pk=pk)
