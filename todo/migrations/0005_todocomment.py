# Generated by Django 5.1 on 2024-08-16 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todostatushistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='todo.todo')),
            ],
        ),
    ]
