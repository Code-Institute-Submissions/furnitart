# Generated by Django 3.0.7 on 2020-07-01 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200701_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='product',
            name='length',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.IntegerField(default=20),
        ),
    ]
