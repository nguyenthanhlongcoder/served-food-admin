# Generated by Django 3.2.5 on 2021-09-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_extravariationoption_extra'),
        ('orders', '0004_auto_20210918_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='extras',
            field=models.ManyToManyField(blank=True, null=True, related_name='extras', to='products.Extra'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order_extra_total_price_record',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order_product_total_price_record',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
