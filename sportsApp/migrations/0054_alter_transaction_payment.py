# Generated by Django 4.2.7 on 2024-08-24 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0053_alter_payment_transaction_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='sportsApp.payment'),
        ),
    ]