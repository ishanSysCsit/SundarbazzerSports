# Generated by Django 4.2.7 on 2024-08-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0035_alter_event_event_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
