# Generated by Django 4.0.2 on 2022-06-01 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('womenwear', '0024_orderplaced_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='order_id',
        ),
    ]
