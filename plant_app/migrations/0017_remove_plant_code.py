# Generated by Django 4.0.5 on 2022-06-29 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0016_alter_plant_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='code',
        ),
    ]