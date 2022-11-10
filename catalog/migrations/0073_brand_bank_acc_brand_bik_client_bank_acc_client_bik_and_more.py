# Generated by Django 4.1.2 on 2022-10-31 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0072_brand_bank_client_bank_organisation_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='bank_acc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='bik',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='bank_acc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='bik',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='bank_acc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='bik',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
