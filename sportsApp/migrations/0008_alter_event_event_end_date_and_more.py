# Generated by Django 4.2.16 on 2024-11-13 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0007_event_status_match_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_start_date',
            field=models.DateTimeField(),
        ),
    ]
