# Generated by Django 3.2.7 on 2021-09-15 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20210915_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('table_id', models.IntegerField()),
                ('order_total_price', models.PositiveBigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talbe_id', models.IntegerField()),
                ('total_price', models.PositiveBigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('order_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item_records', to='orders.orderrecord')),
            ],
        ),
    ]
