# Generated by Django 5.1.7 on 2025-04-11 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply_chain_app', '0006_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supply_chain_app.customer'),
        ),
    ]
