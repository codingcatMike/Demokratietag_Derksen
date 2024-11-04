from django.db import models

# Create your models here.
class Person(models.Model):
    surname = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255, default='')
    exit_time = models.TimeField(null=True, blank=True, default=None)
    entry_time = models.TimeField(null=True, blank=True, default=None)
    verbleibende_zeit = models.CharField(max_length=255, default='')
    person_id = models.IntegerField(null=True, default=None)
    klasse = models.CharField(max_length=255, default='')
    lehrer = models.CharField(max_length=255, default='')
    raum = models.CharField(max_length=255, default='')
    projekt = models.CharField(max_length=255, default='')
    anreise = models.CharField(max_length=255, default='')
    thiersee = models.CharField(max_length=255, default='')
    dinge = models.CharField(max_length=255, default='')
    brotzeit = models.CharField(max_length=255, default='')
    handy = models.CharField(max_length=255, default='')
    anzahl = models.IntegerField(null=True, default=None)
    getraenk = models.CharField(max_length=255, default='')
    completename = models.CharField(max_length=255, default='')
    in_or_out =  models.CharField(max_length=3, default='')
    times_in =  models.IntegerField(null=True, default=None)

