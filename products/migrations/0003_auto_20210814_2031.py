# Generated by Django 3.2.5 on 2021-08-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210814_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='varitation',
            name='price_affected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='variationoption',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='varitation',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
