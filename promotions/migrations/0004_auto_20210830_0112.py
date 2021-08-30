# Generated by Django 3.2.5 on 2021-08-30 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0003_remove_promotion_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AddField(
            model_name='promotion',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
