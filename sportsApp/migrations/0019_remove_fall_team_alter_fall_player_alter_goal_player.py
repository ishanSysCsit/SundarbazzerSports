# Generated by Django 4.2.16 on 2024-11-29 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0018_alter_goal_match'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fall',
            name='team',
        ),
        migrations.AlterField(
            model_name='fall',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fouls', to='sportsApp.player'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='sportsApp.player'),
        ),
    ]
