# Generated by Django 4.2.7 on 2024-07-26 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0013_alter_team_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/teams/'),
        ),
    ]
