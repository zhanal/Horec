# Generated by Django 4.1.1 on 2022-09-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_catalog_customs_tax_catalog_hs_code_catalog_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='customs_tax',
            field=models.FloatField(default=1.5, null=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='margin_coefficient',
            field=models.FloatField(default=1.5, null=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='transport_coefficient',
            field=models.FloatField(default=1, null=True),
        ),
    ]
