# Generated by Django 4.1.1 on 2022-10-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0048_alter_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='order_items', to='catalog.orderitem'),
        ),
    ]
