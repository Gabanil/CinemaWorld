# Generated by Django 4.2 on 2023-05-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0010_alter_reservation_client_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='client_email',
            field=models.EmailField(max_length=254),
        ),
    ]
