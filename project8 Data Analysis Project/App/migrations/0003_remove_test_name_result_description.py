# Generated by Django 3.1.7 on 2021-03-12 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20210311_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test_name',
            name='Result_Description',
        ),
    ]
