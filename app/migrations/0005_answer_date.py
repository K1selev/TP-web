# Generated by Django 4.1.2 on 2022-11-16 21:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_question_date_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
