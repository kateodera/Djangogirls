# Generated by Django 2.2.6 on 2019-11-04 06:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191104_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 4, 6, 57, 13, 106710, tzinfo=utc)),
        ),
    ]
