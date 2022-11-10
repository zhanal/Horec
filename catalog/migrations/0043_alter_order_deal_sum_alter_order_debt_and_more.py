# Generated by Django 4.1.1 on 2022-10-11 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0042_rename_orderproduct_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deal_sum',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='debt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='static/files'),
        ),
        migrations.AlterField(
            model_name='order',
            name='not_shipped',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='profit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='received',
            field=models.IntegerField(default=0),
        ),
    ]
