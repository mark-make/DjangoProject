# Generated by Django 2.0 on 2018-03-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20180322_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='password',
            field=models.CharField(default=0, max_length=256, verbose_name='password'),
        ),
    ]
