# Generated by Django 4.2.16 on 2024-11-15 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0014_alter_team_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='schedule',
            field=models.BooleanField(default=False),
        ),
    ]