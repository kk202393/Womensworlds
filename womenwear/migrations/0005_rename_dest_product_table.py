# Generated by Django 4.0.2 on 2022-04-11 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('womenwear', '0004_dest_main_cat_dest_sub_cat'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='dest',
            new_name='product_table',
        ),
    ]
