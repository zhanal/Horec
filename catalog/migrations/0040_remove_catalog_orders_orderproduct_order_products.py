# Generated by Django 4.1.1 on 2022-10-11 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0039_zone_catalog_zone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='orders',
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.catalog')),
            ],
        ),
    ]
