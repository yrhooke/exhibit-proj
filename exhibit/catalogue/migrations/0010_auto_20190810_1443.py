# Generated by Django 2.2.4 on 2019-08-10 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_auto_20190809_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=64, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='location',
            name='zip_code',
            field=models.CharField(blank=True, max_length=5, verbose_name='zip code'),
        ),
    ]
