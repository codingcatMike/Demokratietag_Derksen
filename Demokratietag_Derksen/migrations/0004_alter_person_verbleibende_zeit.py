# Generated by Django 5.1.1 on 2024-10-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demokratietag_Derksen', '0003_alter_person_verbleibende_zeit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='verbleibende_zeit',
            field=models.CharField(max_length=255),
        ),
    ]
