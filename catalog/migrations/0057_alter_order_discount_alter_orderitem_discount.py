# Generated by Django 4.1.1 on 2022-10-21 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0056_alter_order_discount_alter_orderitem_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='discount',
            field=models.FloatField(blank=True, default=3, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
