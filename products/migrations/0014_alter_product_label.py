# Generated by Django 3.2.5 on 2021-08-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20210830_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.ManyToManyField(blank=True, null=True, related_name='label', to='products.Label'),
        ),
    ]