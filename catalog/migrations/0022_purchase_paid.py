# Generated by Django 4.1.1 on 2022-10-03 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_alter_clients_info_client_purchase_brands_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='paid',
            field=models.IntegerField(null=True),
        ),
    ]
