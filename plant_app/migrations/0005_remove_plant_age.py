# Generated by Django 4.0.5 on 2022-06-16 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0004_plantimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='age',
        ),
    ]