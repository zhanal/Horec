# Generated by Django 4.1.1 on 2022-09-29 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_remove_catalog_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cat',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='catalog',
            old_name='cat',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='cat',
            new_name='category',
        ),
    ]
