# Generated by Django 5.0.2 on 2024-02-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis_app', '0005_alter_thesis_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='publish',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
