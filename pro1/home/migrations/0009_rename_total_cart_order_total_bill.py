# Generated by Django 4.1.3 on 2023-01-01 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_order_total_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_cart',
            new_name='total_bill',
        ),
    ]
