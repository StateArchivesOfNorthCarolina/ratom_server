# Generated by Django 2.2.7 on 2020-01-18 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratom', '0003_auto_20200117_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachments',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratom.Message'),
        ),
    ]
