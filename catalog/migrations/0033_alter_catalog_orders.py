# Generated by Django 4.1.1 on 2022-10-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0032_details_alter_catalog_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='orders',
            field=models.ManyToManyField(related_name='orders', through='catalog.Details', to='catalog.order'),
        ),
    ]
