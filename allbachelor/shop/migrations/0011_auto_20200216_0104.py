# Generated by Django 2.2.5 on 2020-02-15 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200216_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category/%Y/%m/%d'),
        ),
    ]
