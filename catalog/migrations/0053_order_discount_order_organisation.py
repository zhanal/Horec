# Generated by Django 4.1.1 on 2022-10-21 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0052_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.FloatField(default=1.3),
        ),
        migrations.AddField(
            model_name='order',
            name='organisation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.organisation'),
        ),
    ]
