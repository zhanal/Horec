# Generated by Django 4.1.2 on 2022-11-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0075_brand_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='contact_person',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
