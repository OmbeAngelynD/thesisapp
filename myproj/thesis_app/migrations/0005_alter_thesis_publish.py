# Generated by Django 5.0.2 on 2024-02-12 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis_app', '0004_alter_thesis_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='publish',
            field=models.DateTimeField(default=datetime.timezone),
        ),
    ]