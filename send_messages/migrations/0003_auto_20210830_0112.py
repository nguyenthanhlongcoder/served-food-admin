# Generated by Django 3.2.5 on 2021-08-30 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_messages', '0002_auto_20210826_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendmessage',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='sendmessage',
            name='name',
            field=models.TextField(null=True),
        ),
    ]
