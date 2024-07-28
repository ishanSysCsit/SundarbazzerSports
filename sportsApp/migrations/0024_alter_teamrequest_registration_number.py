# Generated by Django 4.2.7 on 2024-07-28 14:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0023_teamrequest_registration_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamrequest',
            name='registration_number',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
