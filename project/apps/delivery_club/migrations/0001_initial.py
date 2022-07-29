# Generated by Django 3.2.13 on 2022-07-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('row_id', models.BigIntegerField()),
                ('order_id', models.BigIntegerField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price_in_rub', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('delivery_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Delivery record',
                'verbose_name_plural': 'Delivery records',
            },
        ),
    ]
