# Generated by Django 4.2.16 on 2024-11-09 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
