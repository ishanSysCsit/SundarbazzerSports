# Generated by Django 4.2.16 on 2024-11-10 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0002_team_email'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='player',
            name='unique_jersey_no_per_team',
        ),
    ]
