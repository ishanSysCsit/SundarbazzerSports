# Generated by Django 4.2.16 on 2024-12-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchApp', '0020_matchstatics_matchtimemanager_is_half_time_over'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchtimemanager',
            name='match_end_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
