# Generated by Django 4.1 on 2023-04-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0008_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='bodyType',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='modal',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='paymentoption',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='transmissionType',
            field=models.CharField(default='', max_length=255),
        ),
    ]