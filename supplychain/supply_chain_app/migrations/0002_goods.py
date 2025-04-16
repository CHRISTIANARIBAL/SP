# Generated by Django 5.1.7 on 2025-04-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply_chain_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
