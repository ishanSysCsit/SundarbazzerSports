# Generated by Django 4.2.7 on 2024-07-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0008_teamrequest_remove_team_team_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.PositiveIntegerField(),
        ),
    ]
