# Generated by Django 3.2.5 on 2021-08-31 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0008_remove_table_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
