# Generated by Django 4.0.2 on 2022-04-09 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='img')),
                ('desc', models.TextField()),
                ('art_no', models.CharField(max_length=30)),
            ],
        ),
    ]
