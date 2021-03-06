# Generated by Django 4.0.5 on 2022-06-16 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0003_plant_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plantImage', to='plant_app.plant')),
            ],
        ),
    ]
