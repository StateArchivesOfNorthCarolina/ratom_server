# Generated by Django 2.2.7 on 2020-01-18 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_size',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='historicalfile',
            name='file_size',
            field=models.BigIntegerField(null=True),
        ),
    ]
