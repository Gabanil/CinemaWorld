# Generated by Django 4.2 on 2023-05-16 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_remove_session_hall_id_remove_session_movie_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='session_id',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='cinema.session', verbose_name='Сеанс'),
        ),
    ]
