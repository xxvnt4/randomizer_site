# Generated by Django 4.0.5 on 2022-06-26 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rand', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='learning',
            options={'verbose_name': 'topic', 'verbose_name_plural': 'topics'},
        ),
        migrations.AddField(
            model_name='learning',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 26, 14, 49, 11, 878526)),
        ),
        migrations.AddField(
            model_name='learning',
            name='date_watched',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 26, 14, 49, 11, 878596)),
        ),
        migrations.AlterField(
            model_name='learning',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
