# Generated by Django 4.0.6 on 2022-08-27 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0006_measurement_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='picture',
            field=models.ImageField(max_length=20, upload_to='pictures/'),
        ),
    ]
