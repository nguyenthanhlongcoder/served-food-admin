# Generated by Django 3.2.5 on 2021-08-30 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0007_auto_20210830_0112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='order',
        ),
    ]
