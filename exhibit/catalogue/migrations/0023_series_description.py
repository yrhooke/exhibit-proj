# Generated by Django 2.2.4 on 2019-10-26 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0022_auto_20191025_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
    ]
