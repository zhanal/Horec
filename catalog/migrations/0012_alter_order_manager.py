# Generated by Django 4.1.1 on 2022-09-29 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_remove_order_brand_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.userprofile'),
        ),
    ]
