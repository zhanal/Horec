# Generated by Django 4.1.1 on 2022-10-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0027_remove_order_product_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients_info',
            name='client',
        ),
        migrations.RenameField(
            model_name='brand',
            old_name='brand',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client',
            new_name='name',
        ),
        migrations.AddField(
            model_name='brand',
            name='contact_person',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='brand',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='contact_person',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Brands_info',
        ),
        migrations.DeleteModel(
            name='Clients_info',
        ),
    ]
