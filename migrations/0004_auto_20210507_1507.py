# Generated by Django 3.0.3 on 2021-05-07 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid_care', '0003_auto_20210506_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plasmadonor',
            name='address',
        ),
        migrations.RemoveField(
            model_name='plasmadonor',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='plasmadonor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='plasmadonor',
            name='other_contact',
        ),
        migrations.RemoveField(
            model_name='plasmadonor',
            name='pin_code',
        ),
    ]
