# Generated by Django 4.2.16 on 2024-09-30 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0077_match_match_time_alter_match_match_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_color', models.CharField(blank=True, max_length=100, null=True)),
                ('secondary_color', models.CharField(blank=True, max_length=100, null=True)),
                ('jersey_number_color', models.CharField(blank=True, max_length=100, null=True)),
                ('neckline_color', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsApp.team')),
            ],
        ),
    ]
