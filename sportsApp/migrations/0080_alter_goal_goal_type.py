# Generated by Django 4.2.16 on 2024-09-30 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0079_alter_teamdesign_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_type',
            field=models.CharField(choices=[('Open Play', 'Open Play'), ('Header', 'Header'), ('Penalty Goal', 'Penalty'), ('Free-Kick Goal', 'Free Kick'), ('Own Goal', 'Own Goal'), ('Volley', 'Volley'), ('Tap-In', 'Tap In'), ('Long-Range Goal', 'Long Range'), ('Chip', 'Chip'), ('Bicycle Kick', 'Bicycle Kick')], default='Open Play', max_length=20),
        ),
    ]
