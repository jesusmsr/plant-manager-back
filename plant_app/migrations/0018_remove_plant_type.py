# Generated by Django 4.0.5 on 2022-06-29 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0017_remove_plant_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='type',
        ),
    ]
