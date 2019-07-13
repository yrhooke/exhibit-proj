# Generated by Django 2.2 on 2019-07-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='price_usd',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price in US Dollars'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='price_nis',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price in NIS'),
        ),
    ]