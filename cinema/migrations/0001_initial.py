# Generated by Django 4.2 on 2023-10-13 14:47

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Імʼя')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Вік')),
                ('description', models.TextField(verbose_name='Опис')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Зображення')),
            ],
            options={
                'verbose_name': 'Актори та режисери',
                'verbose_name_plural': 'Актори та режисери',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категорія')),
                ('description', models.TextField(verbose_name='Опис')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Імʼя')),
                ('description', models.TextField(verbose_name='Опис')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанри',
            },
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True, verbose_name='Номер залу')),
                ('stage', models.IntegerField(verbose_name='Етаж')),
                ('places', models.IntegerField(verbose_name='Кіл-ть місць')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Зали',
            },
        ),
        migrations.CreateModel(
            name='Hall_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='Тип залу')),
            ],
            options={
                'verbose_name': 'Тип залу',
                'verbose_name_plural': 'Тип залів',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Опис')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Постер')),
                ('year', models.PositiveSmallIntegerField(default=2019, verbose_name='Дата виходу')),
                ('country', models.CharField(max_length=30, verbose_name='Країна')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='Премʼєра в світі')),
                ('duration', models.IntegerField(verbose_name='Тривалість')),
                ('available', models.BooleanField(verbose_name='Доступний')),
                ('future', models.BooleanField(verbose_name='Майбутні')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='cinema.actor', verbose_name='Актори')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.category', verbose_name='Категорія')),
                ('directors', models.ManyToManyField(related_name='film_director', to='cinema.actor', verbose_name='Режисер')),
                ('genres', models.ManyToManyField(to='cinema.genre', verbose_name='Жанри')),
            ],
            options={
                'verbose_name': 'Фільм',
                'verbose_name_plural': 'Фільми',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='Початок')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Кінець')),
                ('hall_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.hall', verbose_name='Зал')),
                ('movie_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.movie', verbose_name='Фільм')),
            ],
            options={
                'verbose_name': 'Сеанс',
                'verbose_name_plural': 'Сеанси',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100, verbose_name='Імʼя клієнта')),
                ('client_email', models.EmailField(max_length=254)),
                ('client_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('place_num', models.CharField(max_length=50, verbose_name='Місце')),
                ('paid', models.BooleanField(blank=True, default=False, verbose_name='Оплачено')),
                ('date_resevation', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата та час')),
                ('session_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cinema.session', verbose_name='Сеанс')),
            ],
            options={
                'verbose_name': 'Резервація',
                'verbose_name_plural': 'Резервації',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Опис')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='Зображення')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.movie', verbose_name='Фільм')),
            ],
            options={
                'verbose_name': 'Кадр з фільму',
                'verbose_name_plural': 'Кадри з фільму',
            },
        ),
        migrations.AddField(
            model_name='hall',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cinema.hall_type', verbose_name='Тип залу'),
        ),
    ]
