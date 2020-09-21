# Generated by Django 3.0.7 on 2020-09-21 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0017_auto_20200921_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preorder',
            name='expired',
        ),
        migrations.AddField(
            model_name='preorder',
            name='status',
            field=models.CharField(choices=[('PEND', 'Pending'), ('INV', 'Invalid or experired'), ('UPG', 'Upgraded to order')], default='PEND', max_length=9),
        ),
    ]
