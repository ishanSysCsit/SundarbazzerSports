# Generated by Django 4.2.16 on 2024-11-13 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('sportsApp', '0009_rename_default_address_event_area_event_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='area',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.district'),
        ),
        migrations.AlterField(
            model_name='event',
            name='municipality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.municipality'),
        ),
        migrations.AlterField(
            model_name='event',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.province'),
        ),
    ]
