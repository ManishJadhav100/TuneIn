# Generated by Django 3.2.16 on 2023-05-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicPlayer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='category',
        ),
        migrations.RemoveField(
            model_name='song',
            name='release_year',
        ),
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
