# Generated by Django 2.1.1 on 2018-09-26 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0012_auto_20180926_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='asset',
        ),
    ]