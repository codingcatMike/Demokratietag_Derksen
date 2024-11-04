from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Person

berlin_time = None
from django.shortcuts import redirect

from .models import *


def ShowPers(request):
    return render(request, "Pers.html")


def startpage(request):
    return render(request, "index.html")


def ShowPers(request):
    person = Person.objects.all()
    return render(request, "PersShow.html", {"person": person})


def check(request):
    person = Person.objects.all()
    return render(request, "check.html", {"Person": person})


def delete_database(request):
    Person.objects.all().delete()
    messages.success(request, "Database deleted successfully")
    return redirect("startpage")


def show(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surename = request.POST.get("surename")
        id = request.POST.get("person_id")
        Person.objects.filter(person_id=id).update(in_or_out="out")
        print("The Person  with id: ", id, " has been outed")

    person = Person.objects.filter(in_or_out="in").order_by("surname", "name")
    return render(request, "show.html", {"person": person})


from django.http import JsonResponse


def update_item(request):
    berlin_tz = ZoneInfo("Europe/Berlin")
    berlin_time = datetime.now(berlin_tz)

    updated = False
    for person in Person.objects.all():
        exit_time = datetime.combine(date.today(), person.exit_time)
        exit_time = exit_time.replace(tzinfo=berlin_tz)  # Make exit_time offset-aware

        berlin_time = berlin_time.replace(
            second=round(berlin_time.second), microsecond=0
        )
        if exit_time > berlin_time:
            verbleibende_Zeit = exit_time - berlin_time
        else:
            vor_ver_Zeit = berlin_time - exit_time
            verbleibende_Zeit = "-" + str(vor_ver_Zeit)

        if person.verbleibende_zeit != str(verbleibende_Zeit):
            person.verbleibende_zeit = str(verbleibende_Zeit)
            person.save()
            updated = True

    return JsonResponse({"updated": updated})


def add(request):
    berlin_tz = ZoneInfo("Europe/Berlin")
    berlin_time = datetime.now(berlin_tz)

    if request.method == "POST":
        surname = request.POST.get("surname")
        name = request.POST.get("name")
        exit_hours = int(request.POST.get("exit_hours"))
        exit_minutes = int(request.POST.get("exit_minutes"))
        klasse = request.POST.get("klasse")
        lehrer = request.POST.get("lehrer")
        raum = request.POST.get("raum")
        projekt = request.POST.get("projekt")
        anreise = request.POST.get("anreise")
        thiersee = request.POST.get("thiersee")
        dinge = request.POST.get("dinge")
        brotzeit = request.POST.get("brotzeit")
        handy = request.POST.get("handy")
        anzahl = request.POST.get("anzahl")
        getraenk = request.POST.get("getraenk")
        completename = request.POST.get("completename")
        person_id = request.POST.get("person_id")

        berlin_time = berlin_time.replace(
            second=round(berlin_time.second), microsecond=0
        )
        exit_time = berlin_time.replace(hour=exit_hours, minute=exit_minutes, second=0)

        print(berlin_time)
        print(exit_time)
        verbleibende_zeit = exit_time - berlin_time
        if verbleibende_zeit.total_seconds() < 0:
            verbleibende_zeit = timedelta(days=1) + verbleibende_zeit
            print(verbleibende_zeit)

        hours, remainder = divmod(verbleibende_zeit.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        verbleibende_zeit_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        print(berlin_time)
        print(verbleibende_zeit)
        if person_id == "":
            person_id_1 = Person.objects.all().order_by('-person_id').first().person_id + 1 if Person.objects.all() else 1
            person = Person(
                surname=surname,
                name=name,
                exit_time=exit_time,
                entry_time=berlin_time,
                verbleibende_zeit=str(verbleibende_zeit),
                person_id=person_id_1,
                klasse=klasse,
                lehrer=lehrer,
                raum=raum,
                projekt=projekt,
                anreise=anreise,
                thiersee=thiersee,
                dinge=dinge,
                brotzeit=brotzeit,
                handy=handy,
                anzahl=anzahl,
                getraenk=getraenk,
                completename=completename,
                in_or_out="in",
                times_in=1,
                
            )
            person.save()

            existing_person = Person.objects.filter(person_id=person_id).first()
        else:
            if existing_person:
                # Wenn die person_id existiert, setze in_or_out auf "in"
                existing_person.in_or_out = "in"
                existing_person.exit_time = exit_time
                existing_person.entry_time = berlin_time
                existing_person.verbleibende_zeit = str(verbleibende_zeit)
                existing_person.times_in = existing_person.times_in + 1

                existing_person.save()  # Speichern der Änderungen
                messages.success(request, "Person updated successfully")
      
            

    return render(request, "add.html")
