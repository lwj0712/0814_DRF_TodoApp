# Generated by Django 5.1 on 2024-08-16 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(default=1),
        ),
    ]
