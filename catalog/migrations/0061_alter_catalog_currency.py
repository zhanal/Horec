# Generated by Django 4.1.1 on 2022-10-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0060_alter_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='currency',
            field=models.CharField(choices=[('KZT', 'тг'), ('EUR', 'EUR'), ('USD', 'USD')], default='KZT', max_length=10),
        ),
    ]
