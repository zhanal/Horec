# Generated by Django 4.1.2 on 2022-11-06 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0081_alter_catalog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategories', to='catalog.subcategory'),
        ),
    ]
