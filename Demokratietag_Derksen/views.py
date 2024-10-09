from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Person
from datetime import datetime, timedelta
from datetime import date
from django.http import HttpResponse
import time


def startpage(request):
    return render(request, 'index.html')

def check(request):
    return render(request, 'check.html')

def IBEK(request):
    return render(request, 'IBEK.html')

def show(request):
    if request.method  == 'POST':
        name = request.POST.get('name')
        surename = request.POST.get('surename')
        id = request.POST.get('person_id')
        Person.objects.filter(person_id = id).delete()
        print('The Person  with id: ', id, ' has been deleted')

    person = Person.objects.all()
    return render(request, 'show.html', {'person': person})

from django.http import JsonResponse

def update_item(request):
    updated = False
    for person in Person.objects.all():
        exit_time = datetime.combine(date.today(), person.exit_time)
        current_time = datetime.now()
        current_time = current_time.replace(second=round(current_time.second), microsecond=0)
        if exit_time > current_time:
            verbleibende_Zeit = exit_time - current_time
        else:
            vor_ver_Zeit = current_time - exit_time
            verbleibende_Zeit = '-' + str(vor_ver_Zeit)
        
        if person.verbleibende_zeit != str(verbleibende_Zeit):
            person.verbleibende_zeit = str(verbleibende_Zeit)
            person.save()
            updated = True
    
    return JsonResponse({'updated': updated})

def add(request):
    if Person.objects.exists():
        max_id = Person.objects.all().order_by('-person_id')[0].person_id
        max = max_id + 1
        print(max_id)
        print(max)
    else:
        max = 0

    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        exit_hours = int(request.POST.get('exit_hours'))
        exit_minutes = int(request.POST.get('exit_minutes'))
        completename = request.POST.get('completename')  
        current_time = datetime.now()
        current_time = current_time.replace(second=round(current_time.second), microsecond=0)
        exit_time = current_time.replace(hour=exit_hours, minute=exit_minutes, second=0)
  
        print(current_time)
        print(exit_time)
        verbleibende_zeit = exit_time - current_time
        if verbleibende_zeit.total_seconds() < 0:
            verbleibende_zeit = timedelta(days=1) + verbleibende_zeit
            print(verbleibende_zeit)
        hours, remainder = divmod(verbleibende_zeit.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        verbleibende_zeit_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        print(current_time)
        print(verbleibende_zeit)
        person = Person(surname=surname, name=name, exit_time=exit_time, entry_time=current_time, verbleibende_zeit=str(verbleibende_zeit), person_id=max)
        person.save()
        messages.success(request, 'Person added successfully')
    return render(request, 'add.html')
        