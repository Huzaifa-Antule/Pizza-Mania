# Generated by Django 4.1.3 on 2023-01-01 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_order_total_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='onion',
            field=models.TextField(default='-'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='sweet',
            field=models.TextField(default='-'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='total_cart',
            field=models.TextField(),
        ),
    ]
