# Generated by Django 5.0.1 on 2024-11-01 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demokratietag_Derksen', '0006_person_anreise_person_anzahl_person_brotzeit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='times_in',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
