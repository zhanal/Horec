# Generated by Django 4.1.2 on 2022-10-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0066_alter_purchase_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, related_name='purchase_items', to='catalog.purchaseditem'),
        ),
    ]
