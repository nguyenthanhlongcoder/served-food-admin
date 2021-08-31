# Generated by Django 3.2.5 on 2021-08-31 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20210830_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('serving', 'Serving'), ('paid', 'Paid'), ('cancelled', 'Cancelled')], default='serving', max_length=100),
        ),
    ]
