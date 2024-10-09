# Generated by Django 5.1.1 on 2024-10-03 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('exit_time', models.IntegerField(null=True)),
                ('entry_time', models.IntegerField(null=True)),
                ('verbleibende_zeit', models.IntegerField(null=True)),
            ],
        ),
    ]
