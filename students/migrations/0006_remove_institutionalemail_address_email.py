# Generated by Django 2.2.1 on 2019-06-28 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20190628_0614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institutionalemail',
            name='address_email',
        ),
    ]