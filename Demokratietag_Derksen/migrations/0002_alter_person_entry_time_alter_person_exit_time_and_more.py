# Generated by Django 5.1.1 on 2024-10-03 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demokratietag_Derksen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='entry_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='exit_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='verbleibende_zeit',
            field=models.TimeField(null=True),
        ),
    ]
