# Generated by Django 2.2 on 2019-08-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20190809_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(null=True, upload_to='.'),
        ),
    ]
