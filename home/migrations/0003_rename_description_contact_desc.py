# Generated by Django 4.1.3 on 2022-11-12 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contact_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='description',
            new_name='desc',
        ),
    ]
