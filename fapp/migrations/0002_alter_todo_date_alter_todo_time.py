# Generated by Django 5.0.7 on 2024-07-14 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='Time',
            field=models.TimeField(),
        ),
    ]
