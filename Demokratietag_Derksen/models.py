from django.db import models

# Create your models here.
class Person(models.Model):
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    exit_time = models.TimeField(null=True, blank=True)
    entry_time = models.TimeField(null=True, blank=True)
    verbleibende_zeit = models.CharField(max_length=255)
    person_id = models.IntegerField(null=True)

    