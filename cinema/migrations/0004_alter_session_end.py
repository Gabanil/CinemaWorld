# Generated by Django 4.2 on 2023-05-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_hall_hall_type_reservation_movie_duration_session_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Кінець'),
        ),
    ]
