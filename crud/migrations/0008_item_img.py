# Generated by Django 4.1 on 2023-04-26 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='img',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
