# Generated by Django 2.2.5 on 2019-09-11 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='item',
            field=models.CharField(max_length=200),
        ),
    ]
