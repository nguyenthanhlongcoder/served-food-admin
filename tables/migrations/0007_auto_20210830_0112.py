# Generated by Django 3.2.5 on 2021-08-30 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0006_table_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='status',
            field=models.CharField(choices=[('ready', 'Ready'), ('in_user', 'In User'), ('ordered', 'Ordered')], default='ready', max_length=100),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]