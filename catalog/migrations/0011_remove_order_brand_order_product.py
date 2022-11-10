# Generated by Django 4.1.1 on 2022-09-28 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_remove_catalog_ordered_free_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='brand',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.catalog'),
        ),
    ]
