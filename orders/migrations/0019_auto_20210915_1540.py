# Generated by Django 3.2.7 on 2021-09-15 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_orderitemrecord_orderrecord'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderItemRecord',
        ),
        migrations.DeleteModel(
            name='OrderRecord',
        ),
    ]
