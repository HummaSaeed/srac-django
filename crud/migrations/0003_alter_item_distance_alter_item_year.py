# Generated by Django 4.1 on 2023-04-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_remove_item_amount_remove_item_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='distance',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='year',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
