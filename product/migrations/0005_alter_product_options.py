# Generated by Django 3.2.5 on 2021-07-29 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210714_1843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id',)},
        ),
    ]