# Generated by Django 2.2.5 on 2020-01-15 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
