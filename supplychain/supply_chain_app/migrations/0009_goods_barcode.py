# Generated by Django 5.1.7 on 2025-04-15 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply_chain_app', '0008_alter_goods_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='barcode',
            field=models.CharField(default='000000', max_length=255),
        ),
    ]
