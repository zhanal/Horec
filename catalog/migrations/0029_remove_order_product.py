# Generated by Django 4.1.1 on 2022-10-06 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_remove_clients_info_client_rename_brand_brand_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]
